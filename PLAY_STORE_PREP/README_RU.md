# ZIGRUSH — подготовка Google Play

## Что уже подготовлено
- Rewarded-реклама: игрок сам нажимает «Видео — продолжить» после столкновения.
- Награда выдаётся только после успешного rewarded-показа.
- Продолжение доступно один раз за заезд.
- После рекламы очищается безопасная зона и даётся ~2,2 секунды защиты.
- TEST APK использует официальные тестовые ID Google.
- Отдельный workflow `release-aab.yml` готов для подписанного AAB.

## До публикации
1. Создать приложение ZIGRUSH в AdMob.
2. Создать Rewarded ad unit.
3. В GitHub Secrets добавить `ADMOB_APP_ID` и `ADMOB_REWARDED_ID`.
4. Создать постоянный upload key для Google Play и сохранить его резервную копию.
5. В GitHub Secrets добавить `KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `KEY_ALIAS`, `KEY_PASSWORD`.
6. Настроить Privacy & messaging (UMP/GDPR) в AdMob.
7. Запустить workflow `Build ZIGRUSH RELEASE AAB`.
8. Загрузить `app-release.aab` в Google Play Console.

Важно: не публиковать сборку с тестовыми рекламными ID как финальную версию.
