# D-000021: Stage prepared capture dependencies before a new custody check

**ID:** verifiable-practice:D-000021
**Type:** decision
**Created:** 2026-10-20 08:14:56 UTC
**Author/operator:** Codex worker /root
**Status:** selected; sealed
**Origin:** [D-000020](../D-000020/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-20 08:14:56 UTC

R10actualfirstguard detected new dependencies-before.json created after staging; no blobdifferences, actualcomplete-rootmissingpath and omittedcontrolcontainedextraexpectedpath, exit1. Generalrequirement a custodycheckmust stageallpreparedinputs before comparing, while keeping post-comparison outputs outside the earlierindex claim. Options ignoremissingpath(rejected), overwriteR10(rejected), or preservefailedattemptandnewE11/R11 with preparationstage beforeguard. Select newattempt: captureinitialruntime/dependencies, stagepreparedvp with capturedGitargv/status, then fullguard; afterwardstageoutputs/seals and finalreadonlyguard beforecommit. Existing H9claim remains open until successfulR11. No source product change or stageacceptance reversal; A6scope unchanged, new custodyprojections not independentlyaudited. OwnerpolicyD10/D11/D20delegation; finite26OctUTC/earlier custody/source/tool/authoritytrigger, life+365daysretention. Samehost no authactions/offhostclaim. V11receipt mustlinkfailedR10andnewR11; no remoteoperation/disposal.
