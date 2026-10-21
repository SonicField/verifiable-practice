# Workspace Ownership

Working files are disposable. Relied-on inputs/results must be preserved
with the level-appropriate entry or declared native evidence store and
verified revision replica before completion or cleanup. Raw evidence files
use an owned artefact directory/manifest; an inline D check needs no extra one.

| Location (relative or external physical path) | Owner ID | Operation/last phase | Resume/abort | Retained evidence | Disposition |
|---------------------------------------------|----------|----------------------|--------------|-------------------|-------------|
| <path> | <owner entry> | <process and state> | <safe procedure> | <evidence/manifest when needed> | <level-appropriate entry or disposal commit; V only where required> |

Unknown ownership needs discovery before cleanup. Partial outputs do not
establish completed work.

