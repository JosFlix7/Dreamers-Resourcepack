# Dreamers Resourcepack

Resource pack de Minecraft Java 26.3 en adelante. Aporta los sonidos que usa el plugin Dreamers Triggers, en el namespace `dreamers`.

Hay dos packs en esta repo. Los dos incluyen esos sonidos. Se usa uno u otro, no los dos a la vez.

## Versión simple

Está en la raíz. Es el pack básico del plugin.

- `dreamers:dreamers.effect_fortnite`, en `assets/dreamers/sounds/effect_fortnite.ogg`
- `dreamers:dreamers.effect_bell`, en `assets/dreamers/sounds/effect_bell.ogg`

El mismo namespace trae sonidos y texturas que el plugin todavía no usa: `dreamers:dreamers.effect_rbd`, `dreamers:dreamers.totem` y las texturas de `assets/dreamers/textures/item/`.

## Versión fusionada

Está en `.Dreamers4`. Es el pack que se usa en el servidor. Lleva los mismos assets de `dreamers` y, además, el contenido fusionado de otros resource packs.

## Bedrock

`.bedrock` y `.Dreamers4/.bedrock` son esos assets en formato de Bedrock, para que Geyser se los envíe a los jugadores de esa edición. El pack de Java no les llega.

Geyser conserva el identificador cuando el espacio de nombres no es `minecraft`. Por eso los eventos quedan así:

- `dreamers:dreamers.effect_fortnite`
- `dreamers:dreamers.effect_bell`
