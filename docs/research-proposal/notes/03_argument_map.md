# Argument map
Known: concise reasoning can save generated tokens; style labels do not establish image-grounded explanatory support.
Unknown: does omission-sensitive sufficiency supervision improve accuracy and explicit support beyond style and correctness of stated steps?
Argument: diagnose premise deletion -> define independently checkable sufficiency -> train a calibrated image-conditioned judge -> compare reward signals with shared data/compute -> test robustness and transfer.
Counterarguments: the judge might solve from the image, reward fluent unsupported claims, memorize templates, or penalize alternative proofs. Controls: missing-premise negatives, blind human trace checks, template splits, valid alternative annotations, image ablation, separate final-answer scoring.
Boundary: one 7B model and verifiable diagrams; no causal-faithfulness or universal novelty claim. A null result and a calibrated judge are useful outputs.

Current contrast: four arms share compressed traces, cold-start weights, common budget conditioning, and measured training compute. Separate image-access and omission-negative-training ablations probe mechanisms. The primary decision near 128 achieved tokens combines a ≥3-point accuracy gain and ≥5-point human-sufficiency gain against style, with both paired intervals above zero. The proposal's shortest evidence chain is: identify omitted support → discriminate it from incorrect stated steps → gate the judge → compare policies → independently assess support and image-pair correctness.
