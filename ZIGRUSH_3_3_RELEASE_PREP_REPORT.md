# ZIGRUSH 3.3 — Google Play / Rewarded Ads preparation

- Base: ZIGRUSH 3.1.1 stable gameplay.
- Added `@capacitor-community/admob` 7.2.0 for Capacitor 7.
- Rewarded continue remains optional and is initiated by the player.
- Google test rewarded ID is used in TEST builds.
- AdMob initialization is lazy and does not block initial game startup.
- Reward ad is preloaded after the player starts a normal run.
- A reward is granted only after `showRewardVideoAd()` resolves with a reward.
- One continue per run, ~2.2 seconds invulnerability, nearby obstacles cleared.
- Added separate GitHub Actions workflows for TEST APK and signed RELEASE AAB.
- Release workflow requires permanent signing secrets and live AdMob IDs.
- Added draft Google Play listing text and privacy-policy template.
