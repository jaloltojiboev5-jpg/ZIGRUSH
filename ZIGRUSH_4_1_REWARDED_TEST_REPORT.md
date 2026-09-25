# ZIGRUSH 4.1 — Rewarded Ad Test

Base: ZIGRUSH 4.0 stable (Capacitor 8 / Android API 36).

Changes only:
- Added @capacitor-community/admob 8.1.0 (Capacitor 8 compatible).
- GitHub Actions inserts Google's official TEST AdMob Android app ID into AndroidManifest.xml after Capacitor creates the Android project.
- Uses Google's official Android rewarded TEST ad unit ID already in the game code.
- Continue is granted only after showRewardVideoAd resolves with a reward.
- One rewarded continue per run; nearby obstacles are cleared; 2.2 s invulnerability remains.
- Release AAB workflow is intentionally blocked until test succeeds and production AdMob IDs are available.

Why 3.3 likely crashed:
Google Mobile Ads requires com.google.android.gms.ads.APPLICATION_ID in AndroidManifest.xml. Google documentation says missing this tag causes an app-start crash with "Missing application ID". 3.3 added the native AdMob plugin but the generated manifest was not patched with an app ID.

TEST IDs (do not publish as production):
- Android sample app ID: ca-app-pub-3940256099942544~3347511713
- Rewarded test unit: ca-app-pub-3940256099942544/5224354917
