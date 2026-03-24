#!/usr/bin/env python3
"""
AI Implementation Checklist Tracker

A simple CLI tool to track your progress through the AI implementation checklist.
Stores progress in a local JSON file.

Usage:
    python checklist_tracker.py init          # Initialize a new project
    python checklist_tracker.py status        # Show progress summary
    python checklist_tracker.py phase 1       # Show Phase 1 items
    python checklist_tracker.py check 1.3     # Mark item 1.3 as complete
    python checklist_tracker.py uncheck 1.3   # Mark item 1.3 as incomplete
    python checklist_tracker.py export        # Export progress as markdown
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

PROGRESS_FILE = Path("progress.json")

CHECKLIST = {
    "1": {
        "name": "AI Readiness Assessment",
        "items": {
            "1.1": "Inventory all relevant data sources",
            "1.2": "Assess data quality (completeness, accuracy, consistency)",
            "1.3": "Estimate total data volume",
            "1.4": "Check for data labeling needs",
            "1.5": "Identify data gaps",
            "1.6": "Identify executive sponsor with budget authority",
            "1.7": "Assess in-house ML/AI skills",
            "1.8": "Survey end users",
            "1.9": "Define business problem in measurable terms",
            "1.10": "Confirm AI is the right solution",
            "1.11": "Estimate potential ROI (3 scenarios)",
            "1.12": "Build proof-of-concept",
        },
    },
    "2": {
        "name": "Vendor and Technology Evaluation",
        "items": {
            "2.1": "Decide: build, fine-tune, or use API",
            "2.2": "Compare model capabilities to requirements",
            "2.3": "Evaluate latency requirements",
            "2.4": "Review vendor pricing models",
            "2.5": "Check vendor SLAs",
            "2.6": "Verify data privacy policies",
            "2.7": "Assess vendor lock-in risk",
            "2.8": "Check compliance certifications",
            "2.9": "Determine deployment target (cloud/on-prem/edge)",
            "2.10": "Estimate compute requirements",
        },
    },
    "3": {
        "name": "Development and Integration",
        "items": {
            "3.1": "Design data pipeline",
            "3.2": "Define API contracts",
            "3.3": "Plan model versioning and rollback",
            "3.4": "Implement circuit breakers and fallbacks",
            "3.5": "Design observability (logging, metrics, tracing)",
            "3.6": "Set up reproducible dev environment",
            "3.7": "Establish evaluation metrics tied to business KPIs",
            "3.8": "Create representative test dataset",
            "3.9": "Implement automated testing",
            "3.10": "Implement input validation (prevent prompt injection)",
            "3.11": "Set up API authentication and rate limiting",
        },
    },
    "4": {
        "name": "Testing and Validation",
        "items": {
            "4.1": "Measure accuracy/precision/recall on test data",
            "4.2": "Test with edge cases and adversarial inputs",
            "4.3": "Validate outputs with domain experts",
            "4.4": "Test for bias across demographics",
            "4.5": "Load test at expected peak traffic",
            "4.6": "Test failover behavior",
            "4.7": "Conduct UAT with real end users",
        },
    },
    "5": {
        "name": "Deployment and Monitoring",
        "items": {
            "5.1": "Deploy with gradual rollout strategy",
            "5.2": "Set up monitoring dashboards",
            "5.3": "Document and test rollback procedures",
            "5.4": "Track model drift",
            "5.5": "Monitor for data drift",
            "5.6": "Set up automated alerts for degradation",
            "5.7": "Schedule retraining cycles",
            "5.8": "Track actual vs. projected costs monthly",
        },
    },
}


def load_progress():
    """Load progress from JSON file."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return None


def save_progress(data):
    """Save progress to JSON file."""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def cmd_init(args):
    """Initialize a new project."""
    if PROGRESS_FILE.exists():
        print(f"Progress file already exists: {PROGRESS_FILE}")
        print("Delete it first if you want to start fresh.")
        return

    project_name = input("Project name: ").strip()
    if not project_name:
        print("Project name is required.")
        return

    data = {
        "project_name": project_name,
        "created_at": datetime.now().isoformat(),
        "completed": {},
    }
    save_progress(data)
    print(f"Initialized project: {project_name}")
    print(f"Progress saved to: {PROGRESS_FILE}")
    print(f"\nTotal checklist items: {sum(len(p['items']) for p in CHECKLIST.values())}")
    print("Run 'python checklist_tracker.py status' to see your progress.")


def cmd_status(args):
    """Show progress summary."""
    data = load_progress()
    if not data:
        print("No project initialized. Run: python checklist_tracker.py init")
        return

    completed = data.get("completed", {})
    total_items = sum(len(phase["items"]) for phase in CHECKLIST.values())
    total_done = len(completed)

    print(f"\nProject: {data['project_name']}")
    print(f"Started: {data['created_at'][:10]}")
    print(f"Overall: {total_done}/{total_items} ({100*total_done//total_items}%)")
    print()

    for phase_num, phase in CHECKLIST.items():
        phase_items = len(phase["items"])
        phase_done = sum(1 for k in phase["items"] if k in completed)
        bar_len = 20
        filled = int(bar_len * phase_done / phase_items) if phase_items else 0
        bar = "#" * filled + "-" * (bar_len - filled)

        status = "DONE" if phase_done == phase_items else f"{phase_done}/{phase_items}"
        print(f"  Phase {phase_num}: {phase['name']}")
        print(f"    [{bar}] {status}")
    print()


def cmd_phase(args):
    """Show items in a specific phase."""
    data = load_progress()
    if not data:
        print("No project initialized. Run: python checklist_tracker.py init")
        return

    phase_num = args.number
    if phase_num not in CHECKLIST:
        print(f"Invalid phase: {phase_num}. Valid phases: {', '.join(CHECKLIST.keys())}")
        return

    phase = CHECKLIST[phase_num]
    completed = data.get("completed", {})

    print(f"\nPhase {phase_num}: {phase['name']}")
    print("-" * 50)

    for item_id, description in phase["items"].items():
        done = "[x]" if item_id in completed else "[ ]"
        timestamp = ""
        if item_id in completed:
            timestamp = f"  (completed {completed[item_id][:10]})"
        print(f"  {done} {item_id}: {description}{timestamp}")
    print()


def cmd_check(args):
    """Mark an item as complete."""
    data = load_progress()
    if not data:
        print("No project initialized. Run: python checklist_tracker.py init")
        return

    item_id = args.item
    # Validate item exists
    found = False
    for phase in CHECKLIST.values():
        if item_id in phase["items"]:
            found = True
            description = phase["items"][item_id]
            break

    if not found:
        print(f"Invalid item: {item_id}")
        return

    if "completed" not in data:
        data["completed"] = {}

    data["completed"][item_id] = datetime.now().isoformat()
    save_progress(data)
    print(f"Checked: {item_id} - {description}")


def cmd_uncheck(args):
    """Mark an item as incomplete."""
    data = load_progress()
    if not data:
        print("No project initialized. Run: python checklist_tracker.py init")
        return

    item_id = args.item
    completed = data.get("completed", {})

    if item_id in completed:
        del data["completed"][item_id]
        save_progress(data)
        print(f"Unchecked: {item_id}")
    else:
        print(f"Item {item_id} was not checked.")


def cmd_export(args):
    """Export progress as markdown."""
    data = load_progress()
    if not data:
        print("No project initialized. Run: python checklist_tracker.py init")
        return

    completed = data.get("completed", {})

    print(f"# {data['project_name']} — AI Implementation Progress\n")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    for phase_num, phase in CHECKLIST.items():
        phase_done = sum(1 for k in phase["items"] if k in completed)
        print(f"## Phase {phase_num}: {phase['name']} ({phase_done}/{len(phase['items'])})\n")
        for item_id, description in phase["items"].items():
            check = "x" if item_id in completed else " "
            print(f"- [{check}] {description}")
        print()


def main():
    parser = argparse.ArgumentParser(description="AI Implementation Checklist Tracker")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Initialize a new project")
    subparsers.add_parser("status", help="Show progress summary")

    phase_parser = subparsers.add_parser("phase", help="Show items in a phase")
    phase_parser.add_argument("number", help="Phase number (1-5)")

    check_parser = subparsers.add_parser("check", help="Mark item as complete")
    check_parser.add_argument("item", help="Item ID (e.g., 1.3)")

    uncheck_parser = subparsers.add_parser("uncheck", help="Mark item as incomplete")
    uncheck_parser.add_argument("item", help="Item ID (e.g., 1.3)")

    subparsers.add_parser("export", help="Export progress as markdown")

    args = parser.parse_args()

    commands = {
        "init": cmd_init,
        "status": cmd_status,
        "phase": cmd_phase,
        "check": cmd_check,
        "uncheck": cmd_uncheck,
        "export": cmd_export,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
