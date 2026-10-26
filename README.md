# Dreamers Resourcepack

Resource pack de Minecraft Java 26.3 en adelante. Aporta los sonidos que usa el plugin: Dreamers Triggers.

Hay dos packs en esta repo. Los dos incluyen esos sonidos. Se usa uno u otro, no los dos a la vez.

## Versión simple

Está en la raíz. Solo contiene los sonidos, y es el pack básico del plugin.

- `minecraft:terranova.death`, en `assets/minecraft/sounds/terranova/terranova_death.ogg`
- `minecraft:terranova.totem`, en `assets/minecraft/sounds/terranova/terranova_totem.ogg`

## Versión fusionada

Está en `.Dreamers4`. Es el pack que se usa en el servidor. Lleva los mismos sonidos y, además, el contenido fusionado de otros resource packs.

## Bedrock

La carpeta `bedrock` es el mismo par de sonidos en formato de Bedrock, para que Geyser se los envíe a los jugadores de esa edición. El pack de Java no les llega.

Geyser reproduce `terranova.death` y `terranova.totem`, que es como quedan los eventos `minecraft:terranova.death` y `minecraft:terranova.totem` al quitar el espacio de nombres.