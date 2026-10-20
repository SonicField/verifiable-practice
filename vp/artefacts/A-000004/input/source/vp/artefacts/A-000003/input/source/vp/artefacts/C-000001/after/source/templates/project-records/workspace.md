# Workspace Ownership

Working files are disposable. Relied-on inputs/results must be preserved
under the owning record's artefact directory before completion or cleanup.

| Location (relative or external physical path) | Owner ID | Operation/last phase | Resume/abort | Retained evidence | Disposition |
|---------------------------------------------|----------|----------------------|--------------|-------------------|-------------|
| <path> | <ID link> | <process and state> | <safe procedure> | <manifest link> | <V link when removed> |

Unknown ownership needs discovery before cleanup. Partial outputs do not
establish completed work.

