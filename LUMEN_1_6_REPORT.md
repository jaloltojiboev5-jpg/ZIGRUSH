# LUMEN 1.6 — Android build handoff

## Completed
- Preserved LUMEN 1.5 gameplay and settings.
- Added a cloud Android build workflow using GitHub Actions.
- Added repeatable npm/Capacitor Android preparation scripts.
- Added Windows-friendly build documentation.
- The workflow creates a test/debug APK as a downloadable CI artifact.

## Important status
A real APK is **not claimed as already built in this chat**. The supplied workflow performs the actual Android build in a compatible cloud environment.

## Still requiring external accounts/actions
- GitHub account/repository: needed to run the cloud build.
- Google Play Console: needed for publishing.
- AdMob: needed for real rewarded advertising.
- Google Play Billing configuration: needed for real purchases.
- Release signing keystore: needed for production AAB.

## Player features retained
- 5 worlds / 125-level structure
- Stars and move limits
- Hints
- Daily Challenge and Streak
- Achievements
- Shop/economy
- Russian / English / Chinese
- Persistent progress and backup
- Sound ON/OFF
- Vibration ON/OFF
- Mobile/PWA structure
