# AI Readiness Assessment

Fill out this template before starting any AI project. Be honest — overstating readiness leads to failed projects.

## Project Overview

| Field | Your Answer |
|-------|-------------|
| Project name | |
| Business unit | |
| Executive sponsor | |
| Target launch date | |
| Budget range | |

## Problem Statement

**What business problem are you solving?**
> Write 2-3 sentences describing the problem in measurable terms.

**What is the current solution?**
> How is this handled today? Manual process, rule-based system, or nothing?

**Why do you believe AI is the right solution?**
> What makes this problem suitable for AI vs. traditional software?

## Data Assessment

| Question | Answer | Score (1-5) |
|----------|--------|-------------|
| Do you have historical data for this problem? | Yes/No | |
| How much data? (rows/documents/images) | | |
| Is the data labeled/annotated? | Yes/Partially/No | |
| Is the data clean and consistent? | Yes/Mostly/No | |
| Can you access the data programmatically? | Yes/No | |
| Are there privacy/compliance concerns? | Yes/No | |

**Data Score**: Sum of all scores. Below 15 = significant data work needed. 15-25 = moderate prep. 25+ = data-ready.

## Team Assessment

| Role | In-house? | Skill Level (1-5) | Hiring Plan |
|------|-----------|-------------------|-------------|
| ML Engineer | Yes/No | | |
| Data Engineer | Yes/No | | |
| DevOps/MLOps | Yes/No | | |
| Domain Expert | Yes/No | | |
| Product Manager | Yes/No | | |

**Team Score**: Count of roles with skill level 3+. Below 2 = need significant hiring or outsourcing.

## Infrastructure Assessment

| Question | Answer |
|----------|--------|
| Current cloud provider | AWS / GCP / Azure / None |
| GPU access available? | Yes / No |
| CI/CD pipeline exists? | Yes / No |
| Monitoring stack in place? | Yes / No |
| Container orchestration? | Yes / No |

## Risk Assessment

| Risk | Likelihood (1-5) | Impact (1-5) | Mitigation |
|------|-------------------|--------------|------------|
| Data quality issues | | | |
| Model doesn't meet accuracy target | | | |
| Integration complexity | | | |
| User adoption resistance | | | |
| Vendor dependency | | | |
| Regulatory compliance | | | |

## ROI Projection

| Scenario | Annual Savings | Implementation Cost | Payback Period |
|----------|---------------|-------------------|----------------|
| Conservative | $ | $ | months |
| Moderate | $ | $ | months |
| Optimistic | $ | $ | months |

## Overall Readiness Score

| Category | Score | Max |
|----------|-------|-----|
| Data | /30 | 30 |
| Team | /5 | 5 |
| Infrastructure | /5 | 5 |
| Problem clarity | /5 | 5 |
| Budget available | /5 | 5 |
| **Total** | **/50** | **50** |

**Interpretation**:
- **40-50**: Green light — proceed with confidence
- **25-39**: Yellow — address gaps before starting
- **Below 25**: Red — significant preparation needed before an AI project is viable

---

*Template from [ai-implementation-checklist](https://github.com/shift-ai007/ai-implementation-checklist)*
