# ZIGRUSH 3.1.1 STABLE

- Removed native AdMob plugin temporarily because the 3.1 build crashed immediately on launch on the test phone.
- Kept record-only gameplay and one-continue-per-run logic.
- Continue button runs in test mode so the resume/protection mechanic can be verified before ads are re-enabled.
- Launcher icon is copied directly into Android legacy mipmap resources and adaptive XML launchers are removed during CI build.
- After this build is confirmed to launch correctly, rewarded AdMob will be reintroduced with explicit initialization and tested separately.
