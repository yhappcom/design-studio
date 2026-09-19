# I101 — Pre-runtime workflow-authority oracle

Date: 2026-09-20
Purpose: PRACTICE / adversarial closure preparation after I100.

## RELATED DOMAIN CHECK
T082/T083, C113/C114, L104, W113 and CD119 checked. Human usability remains deferred; this is a non-human structural oracle.

## Shared authority chain
Across navigation, search, edit/save, reorder and offline recovery, distinguish: user intent → draft/proposal → validation → requested mutation → pending/unknown outcome → authoritative local/persisted result → sync acknowledgement → refreshed projection → recovery/inverse.

## Five scenario falsifiers
1. Navigation/history: Back/Forward or reload restores a route but silently loses relevant task state or invents it.
2. Search: superseded A response can replace newer B results; active result is confused with selected/opened record.
3. Add Flight: validation/persistence/retry messages outrun authoritative state; blind retry can duplicate an unknown mutation.
4. Reorder: drag and non-drag paths produce different canonical order or recovery; focus loses item identity.
5. Offline/reconnect: offline capability is presented as failure/success; reconnect overwrites an unresolved local mutation without explicit reconciliation.

Focus movement, status feedback, reversibility and recovery ownership must remain explicit at every transition.

## HANDOFFS TO OTHER SPECIALISTS
Content names only states the implementation can prove. Color encodes but does not redefine them. Layout protects object/action/recovery relationships. Web records transaction/history/network provenance. Type renders the complete semantic strings.

## Evidence boundary
No runtime, AT, discoverability, workload, trust or representative-pilot PASS is claimed.