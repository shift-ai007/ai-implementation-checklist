# Example: Customer Support Chatbot

A filled-out checklist example for a B2B SaaS company implementing an AI-powered customer support chatbot.

## Project Overview

| Field | Answer |
|-------|--------|
| Project name | Support Assistant v1 |
| Business unit | Customer Success |
| Executive sponsor | VP of Customer Success |
| Target launch date | Q2 2026 |
| Budget range | $50K-$80K |

## Problem Statement

**Business problem**: Customer support team handles 2,000+ tickets/month. Average first response time is 4 hours. 60% of tickets are repetitive (password resets, billing questions, feature how-tos). Goal: deflect 40% of repetitive tickets with an AI chatbot, reducing first response time to under 2 minutes for common questions.

**Current solution**: Zendesk with canned responses. Agents manually classify and respond. Knowledge base exists but search is poor.

**Why AI**: Pattern recognition across ticket categories. Natural language understanding for intent classification. Ability to pull answers from knowledge base and past tickets dynamically.

## Readiness Scores

| Category | Score | Notes |
|----------|-------|-------|
| Data | 24/30 | 18 months of Zendesk tickets (labeled by category). Some categories under-represented. |
| Team | 3/5 | Backend engineers can build APIs. Need ML expertise for fine-tuning. |
| Infrastructure | 4/5 | AWS, Docker, CI/CD all in place. No GPU instances yet. |
| Problem clarity | 5/5 | Very clear, measurable goal. |
| Budget | 4/5 | Approved, but tight for custom model training. |
| **Total** | **40/50** | Green light |

## Decision: API-Based Approach

Selected **Anthropic Claude API** over custom model because:
1. Budget constraints — fine-tuning a custom model would exceed budget
2. Claude handles conversational Q&A well out of the box with RAG
3. Faster time-to-market (weeks vs. months)
4. No GPU infrastructure needed

## Key Risks Identified

1. **Hallucination** — chatbot might give incorrect answers about product features
   - Mitigation: RAG with verified knowledge base, confidence thresholds, human handoff
2. **User trust** — customers may not trust AI responses
   - Mitigation: Transparent labeling ("AI-generated"), easy escalation to human agent
3. **API costs at scale** — 2,000 tickets × ~500 tokens each × $0.015/1K tokens
   - Mitigation: Caching common responses, shorter context windows for simple queries

## Timeline (Actual)

| Week | What happened |
|------|-------------|
| 1-2 | Knowledge base cleanup, Zendesk data export, API key setup |
| 3-4 | RAG pipeline built (embeddings + vector store + Claude) |
| 5 | Internal testing — 78% accuracy on test set |
| 6 | Improved prompts, added guardrails — 89% accuracy |
| 7 | Beta with 10% of traffic, human review of all responses |
| 8 | Full launch with human escalation path |

## Results After 3 Months

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| First response time | 4 hours | 45 seconds (AI) / 2 hours (human) | -81% average |
| Ticket deflection | 0% | 38% | +38% |
| CSAT score | 3.8/5 | 4.1/5 | +0.3 |
| Monthly support cost | $32K | $24K | -25% |
| AI operating cost | $0 | $1.2K/month | |

---

*Example from [ai-implementation-checklist](https://github.com/shift-ai007/ai-implementation-checklist)*
