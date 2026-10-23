# Skill-based review of the sketch-sufficiency research plan

Reviewed on 2026-10-23. Review target: `docs/research-plan/sketch-sufficiency.html`; source of scientific claims: `docs/presentation/paper/2601.02825.txt`. Source locations below are text-file line numbers and section/table identifiers, not inferred PDF page numbers.

## Skills used

All listed `SKILL.md` files were read. This is a bounded, single-agent review against the assignment, followed by the explicitly requested repairs; it is not an ARS journal panel or an independent multi-reviewer assessment. The assignment's output format and authorization to fix substantive issues take precedence over generic journal-review workflows.

| Collection | Exact skill name and path | Contribution |
|---|---|---|
| academic-research-skills-codex | `academic-research-suite` — `/home/box/.codex/skills/academic-research-suite/SKILL.md` | Routed the review through the academic-paper-reviewer material; applied source verification, evidence-anchored findings, proportional severity, and separation of observation from recommendation. Read `ars/academic-paper-reviewer/WORKFLOW.md` and used `references/review_quality_thinking.md` for internal validity, external validity, and contribution. |
| K-Dense-AI scientific-agent-skills | `scientific-critical-thinking` — `/home/box/.codex/skills/scientific-critical-thinking/SKILL.md` | Checked the gap against the appendix, isolated reward and rewriting confounders, identified judge-label leakage risks, and aligned measurements with each research question. Clinical evidence-grading frameworks do not apply to this ML proposal. |
| Orchestra-Research AI-Research-SKILLs | `brainstorming-research-ideas` — `/home/box/.codex/skills/brainstorming-research-ideas/SKILL.md` | Applied Problem-First Thinking, Failure Analysis and Boundary Probing, and the Simplicity Test to assess the existing idea's contribution relative to SketchThinker-R1. Kept the existing direction; did not generate replacement projects. |
| Supporting process collection | `superpowers:using-superpowers` — `/home/box/.codex/skills/using-superpowers/SKILL.md` | Checked relevant skill guidance and user-instruction priority. |
| Supporting process collection | `superpowers:verification-before-completion` — `/home/box/.codex/skills/verification-before-completion/SKILL.md` | Required fresh build evidence, a `pdfinfo` page count, and final source/output checks before reporting completion. |

The three requested collection memberships were checked through the installed symlink destinations under `/home/box/.codex/skill-repos/`.

## Requirement compliance

| Requirement | Original plan | Final check |
|---|---|---|
| Working Title | Present and specific. | Retained. |
| Problem Statement: 1–2 sentences, original-paper gap | Two sentences; gap overstated the absence of preservation evaluation. | Correct gap while retaining two sentences. |
| Proposed Solution: one paragraph, novel idea and improvement | One paragraph; image-conditioned sufficiency reward and comparison to style supervision were clear. Important operational details were missing. | Keep one paragraph and clarify the experiment. |
| Key Research Questions: 2–3 bullets | Three bullets; third repeated the main comparison and its controls. | Keep three bullets with diagnostic, performance, and visual-dependence questions. |
| Expected Outcome: one sentence | One sentence; improvement is an empirical question rather than a promised positive result. | Retained. |
| Single page | Existing PDF reports `Pages: 1`. | Rebuild and verify below. |

## Issues found and remedies

Severity: **Major** materially affects the scientific motivation or attribution of an effect; **Moderate** makes a proposed measurement or comparison underspecified; **Minor** affects presentation alone. No critical issue was found.

1. **Major — the gap dismisses existing preservation checks.** Original Problem Statement: “leaving the preservation of answer-critical visual evidence unverified.” Section 2.2 supports the narrower observation that SketchJudge receives only a trace (lines 179–202), but Appendix H explicitly checks whether key reasoning steps survive compression: five humans assess 20 cold-start examples (Table 13, lines 1067–1085), and an image-conditioned LVLM evaluates the full cold-start dataset (Table 14, lines 1088–1103). These checks do not constitute the proposed grounded sufficiency reward during RL. **Remedy:** acknowledge the cold-start checks and locate the gap in whether rewarding grounded premises improves the tradeoff of learned traces.

2. **Major — the reward intervention is ambiguous.** “Sufficiency and style rewards will be compared” does not say whether sufficiency replaces the style term or the whole objective. The paper already rewards answer accuracy and response format, in addition to style (Eq. 5, lines 229–233). Changing those terms would confound the claimed benefit. **Remedy:** replace only the style term, retain accuracy and format terms, share initialization and cold-start data, and distinguish the policy-training compute budget from judge construction/scoring costs. Use a common length penalty selected on validation data to obtain comparable reasoning lengths.

3. **Moderate — judge training and validation lack a separation rule and useful negative examples.** “These annotations will train and validate a judge” leaves related images/traces free to cross the split. A judge that can solve the question still needs to detect incomplete or contradicted premises in a trace. **Remedy:** split by underlying problem before constructing image pairs, train with complete and premise-deleted/contradicted traces, and validate against held-out human judgments. Keep alternative valid solution paths in the annotations so verbatim reproduction of one reference chain is not the sufficiency criterion.

4. **Moderate — RQ1's denominator is missing from the method.** The solution mentions premise annotation, but RQ1 compares visual-premise omissions with nonvisual-step omissions. **Remedy:** explicitly annotate both visual premises and nonvisual deductions for valid solution paths, and describe the tested operation as rewriting long traces into sketches.

5. **Moderate — RQ3 repeats RQ2 and does not directly test the proposed visual mechanism.** Matched data/compute are essential controls, already in the solution, rather than a distinct scientific question. “Paired-image correctness” is also undefined. **Remedy:** ask whether gains hold on both versions of answer-changing image pairs and depend on the judge's image access; add an image-blind sufficiency-judge ablation and define pair correctness as getting both answers right. Keep pairs together in the split.

6. **Moderate — feasibility and difficulty groups need operational scope.** “One 7B model” leaves the policy backbone unspecified; “harder items” leaves subgroup selection open after observing outcomes. **Remedy:** name the paper's Qwen2.5-VL-7B-Instruct backbone, scope annotation to a small diagram set, and define difficulty groups before training. This is a scoped experiment, not a replication of the paper's full training suite.

No style-only defects justify changing the title, layout, repeated title label, or expected-outcome sentence. Those are retained.

## Claim and number audit

| Plan assertion or design element | Evidence and disposition |
|---|---|
| SketchJudge receives neither image nor question | Supported by the explicit trace-only prompt in §2.2, lines 185–190, and trace parsing in §2.3, lines 242–248. This concerns the style judge, not the multimodal policy or all evaluation. |
| Preservation is unverified | Too broad; contradicted by Appendix H's key-step preservation evaluations. Corrected as above. The paper's checks concern cold-start data and are not premise-level causal tests of the learned policy. |
| Cold-start data are evaluated for key-step preservation (revised statement) | Supported by Appendix H, Tables 13–14. Table 13 records retained-step counts of 20, 19, 20, 18, and 19 out of 20; Table 14 reports 19,182 retained / 818 missing-key-step judgments out of 20,000. These are evaluator judgments, not proof of universally complete visual grounding. No rates or counts were added to the plan. |
| The paper does not test an explicit grounded-premise reward | §2.2–2.3 and Appendix E specify style-based reward variants; Appendix H evaluates data quality, and Appendix G evaluates interpretability. No grounded-premise RL reward comparison is reported in the supplied text. This is an absence finding bounded to that source. |
| One 7B policy / Qwen2.5-VL-7B-Instruct | A proposed scope choice, consistent with Table 1 (lines 325–331) and Appendix D.1/D.3 (lines 786–787, 801–803). “One” means one policy backbone across experimental arms, not one training run or a claim that the original paper used only one model. The judge is an additional model. |
| Accuracy and format reward terms exist | Eq. 5 reports weights 0.5, 0.4, and 0.1 for accuracy, format, and style. Revised plan retains the first two components; the added common length penalty is a proposed experimental control, not attributed to the paper. |
| Text-only long-to-sketch rewriting | §2.1 and Appendix A/Table 16, especially lines 1165–1199, describe text reasoning compression. The question asks whether visual premises are omitted disproportionately; it does not claim the paper established that failure. |
| Original-trace and length-preserving rewrite controls | Proposed controls. Appendix E already includes a long-trace cold-start baseline (Table 8, lines 930–978), so a long-trace control alone is not claimed as novel. |
| Image pairs, sufficiency labels/judge, omission metrics, compute matching, budget matching, and image-blind ablation | Proposed methods, not reported SketchThinker-R1 results. Pair correctness is now defined; split boundaries and independent human evaluation are explicit. |
| Improvement, especially on harder items | A testable research question and expected evaluation, not an established effect or invented numerical target. |
| SketchThinker-R1 / Zhang, Zhou, Zheng / 2026 | Title, authors, and January 2026 arXiv date appear at the start of the supplied text (lines 6–16). The HTML uses only the short title and venue/year. |
| ICLR 2026 | Supplied explicitly in the user's assignment. The local text labels itself “Preprint” and contains no ICLR confirmation; retained as user-provided context, not claimed as independently verified from the text. |

There are no reported performance numbers in the original or revised plan to recalculate. Its model-size number and venue year are accounted for above.

## Novelty, feasibility, questions, and clarity

**Contribution relative to the supplied paper:** moving from post-hoc cold-start key-step checks to a grounded sufficiency training reward, with premise-level annotations and answer-changing image pairs, is a distinct extension. Merely adding an image-conditioned evaluator would overlap Appendix H. The image-blind ablation tests whether visual access contributes beyond changing judge labels. Global priority relative to all literature is not established by a single-paper comparison; the plan makes no first-ever claim.

**Feasibility:** a single policy backbone and a small, verifiable diagram set constrain the project. Annotation, judge validation, paired-image checking, and several training arms still require real effort and GPU resources. The source's full experiments used eight H200 GPUs (§3, line 272); that is context, not a resource promise for this project. A practical first experiment is to validate the judge's detection of deleted/contradicted premises on held-out problems before starting the policy comparison. Exact sample size and hardware budget belong in the execution protocol; neither is invented here.

**Measurement:** annotate valid solution paths rather than demand a single canonical trace. Use original problems/image-pair families as the held-out unit, retain incorrect and incomplete responses in evaluation, and report paired comparisons with uncertainty in the eventual study. Pair success means both answers are correct; it tests behavior under an image change, not hidden internal reasoning faithfulness. Human checks remain necessary because the learned judge is the training intervention.

**Question quality:** RQ1 diagnoses omission; RQ2 tests the accuracy–length tradeoff and premise retention; RQ3 tests pair robustness and dependence on visual access. All are answerable without presuming the proposed reward wins. Rewriting and compute controls remain in the method.

**Clarity:** use direct factual language for the gap and future-tense language for the intervention. Retain the assignment's five sections, one solution paragraph, and three question bullets. Do not add defensive disclaimers or unsupported performance targets to the plan.

## Fixes applied and verification

Review findings were written before editing the HTML. Applied the six substantive remedies above in the Problem Statement, Proposed Solution, and RQ1/RQ3. Kept RQ2, Working Title, Expected Outcome, and all CSS unchanged. The solution is one paragraph of 182 whitespace-delimited words.

Validation performed:

- Parsed the final HTML: all five required sections; two Problem Statement sentences; one Proposed Solution paragraph; three question bullets; one Expected Outcome sentence.
- Attempted the exact supplied Chrome build command. It failed creating its default profile. A writable temporary profile exposed container socket restrictions (`setsockopt: Operation not permitted`); attempts with Chrome's crash-handler/sandbox startup flags still failed at `sandbox_host_linux.cc` with `shutdown: Operation not permitted`.
- **Build fallback:** rebuilt `docs/research-plan/sketch-sufficiency.pdf` directly from the final HTML body and stylesheet using installed PyMuPDF 2.0 / MuPDF 1.28.5 `Story` and `DocumentWriter`. Embedded the installed Liberation Serif/Sans regular/bold fonts, used a 612 × 792 pt Letter page and the HTML's 0.48 in vertical / 0.58 in horizontal margins, and allowed natural pagination without shrinking text. The PDF creator metadata identifies the fallback. This is a rebuilt PDF, not a successful Chrome build; exact Chrome rendering remains unverified in this container.
- Ran `pdfinfo docs/research-plan/sketch-sufficiency.pdf`: **`Pages: 1`**, `Page size: 612 x 792 pts (letter)`.
- Compared every HTML body character with extracted PDF text after removing whitespace and rendered bullet markers: identical text in order, including the final outcome. All extracted text bounds lie inside the page.
- Rendered the final PDF with `pdftoppm` and inspected it: readable text, all headings and three bullets visible, no clipping or overflow.
- Ran `git diff --check`: clean. No commit made. The pre-existing untracked `.agents/skills/nature-figure/scripts/__pycache__/` was left untouched.

## Skill attribution

Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents*. [arXiv:2609.00065](https://doi.org/10.48550/arXiv.2609.00065). Author list, title, year, and current revision (v2, 2026-09-02) checked against the [arXiv record](https://arxiv.org/abs/2609.00065) on 2026-10-23. This credits the K-Dense skill used in the review; it is not evidence for SketchThinker-R1's claims.
