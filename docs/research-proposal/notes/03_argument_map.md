# Argument map
Known: concise reasoning can save generated tokens; style labels do not establish image-grounded explanatory support.
Unknown: does evidence-aware supervision improve accuracy and necessary-premise retention under compression?
Argument: diagnose premise deletion -> define independently checkable sufficiency -> train a calibrated image-conditioned judge -> compare reward signals with shared data/compute -> test robustness and transfer.
Counterarguments: the judge might solve from the image, reward fluent unsupported claims, memorize templates, or penalize alternative proofs. Controls: missing-premise negatives, blind human trace checks, template splits, valid alternative annotations, image ablation, separate final-answer scoring.
Boundary: one 7B model and verifiable diagrams; no causal-faithfulness or universal novelty claim. A null result and a calibrated judge are useful outputs.
