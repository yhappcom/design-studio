# T021 R1 No-Scope-Creep Contradiction Review

Evidence mode: **CONTRADICTION REVIEW / GATE PROTECTION**.

## Question
Do newer systems studies (authorization, tenant/context switching, retention, audit/export) justify expanding the T021 drawing repair before the bounded R1 raster is executed?

## RELATED DOMAIN CHECK
C049, I036/L040, W049 and CD055 add context/tenant strings and runtime states, but none supplies evidence that the accepted `I/l/1` and candidate-B `0` drawing diagnosis is wrong. Their strings can be exercised with mature fallback while the custom face remains provisional.

## Review
No. Expanding glyph repertoire, operational corpus, spacing or kerning before R1 execution would weaken causal attribution. The current experiment intentionally freezes widths, sidebearings, kerning and unrelated glyphs so any raster change can be attributed to the bounded drawing patch.

New context names and IDs may later become transfer strings, but they are not a reason to alter R1 geometry or reopen the candidate decision now. CD055 strings must not be shortened to fit provisional metrics.

## Gate decision
- R1 patch scope remains only `I/l/1` plus candidate-B `0` slash refinement.
- Kerning remains OFF.
- Widths/sidebearings remain frozen.
- No new corpus expansion is required before R1.
- Next valid evidence remains actual mutation → source/build/font/raster hashes → 14/17/24px direct critique.
- General spacing opens only after drawing is defensible; kerning only after general spacing.

## OPEN
The present connector can edit repository text but cannot safely provide the complete inspectable source→font→raster execution loop needed for this geometry experiment. This is an execution blocker, not evidence of PASS.

## HANDOFFS TO OTHER SPECIALISTS
W049 and CD055 should use mature fallback and preserve full semantic strings. L040 must not freeze layout to provisional custom metrics. C049 must not use color to compensate for ambiguous glyph construction.