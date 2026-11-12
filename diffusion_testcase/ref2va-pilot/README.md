# MiniMax H3 Ref2VA: Five Pilot Cases

Five compact cases for checking reference-role following, identity consistency,
motion transfer, sound conditioning, and multimodal composition. These are a
curated pilot set, not a statistically representative benchmark.

| Case | References | Main check |
| --- | --- | --- |
| 01 | Dog image | Preserve subject identity in a new scene and action |
| 02 | Dog image + forest image | Separate subject identity from environment reference |
| 03 | Dog image + agility video | Keep the image subject while borrowing motion and camera behavior |
| 04 | Dog image + bark audio | Coordinate a visible action with reference sound |
| 05 | Dog image + agility video + bark audio | Compose three reference roles without copying unrelated source content |

Each case prompt is in `cases/`. Shared files are in `assets/raw/` and
`assets/processed/`. The motion reference is a 12-second, 1280x720, 24 FPS,
H.264 MP4 with its source audio removed. The bark reference is a 2.61-second,
mono 44.1 kHz WAV. Both satisfy the H3 Ref2VA media input limits documented in
the MiniMax H3 recipe.

Use the same output duration, resolution, model/checkpoint, and inference
settings across cases. For a quick smoke test, one fixed seed per case is
enough; for a quality comparison, repeat each case with multiple seeds and
score identity, reference adherence, video quality, audio quality, and AV
alignment separately.

## Assets and attribution

| Local file | Source and attribution | License |
| --- | --- | --- |
| `assets/raw/dog_subject.jpg` | [Papillon dog agility jump](https://commons.wikimedia.org/wiki/File:Papillon_dog_agility_jump.jpg), Ron Armstrong, via Flickr | CC BY 2.0 |
| `assets/raw/forest_scene.jpg` | [Clearing, Achnabreck Forest](https://commons.wikimedia.org/wiki/File:Clearing,_Achnabreck_Forest_-_geograph.org.uk_-_15852.jpg), Mick Garratt / geograph.org.uk | CC BY-SA 2.0 |
| `assets/raw/border_collie_agility_source.ogv` | [Pink, the border collie wins back-to-back titles at the 2019 WKC Masters Agility](https://commons.wikimedia.org/wiki/File:Pink,_the_border_collie_wins_back-to-back_titles_at_the_2019_WKC_Masters_Agility_%28FOX_SPORTS%29.ogv), FOX Sports | CC BY 3.0 |
| `assets/processed/dog_agility_motion_12s.mp4` | 12-second video-only excerpt, source interval 76-88 seconds; converted to H.264 at 24 FPS from the FOX Sports Commons file above | CC BY 3.0, adapted from source |
| `assets/raw/dog_bark_source.ogg` | [Barking of a dog](https://commons.wikimedia.org/wiki/File:Barking_of_a_dog.ogg), Amada44 | CC BY-SA 3.0 |
| `assets/processed/dog_bark.wav` | WAV conversion of the Commons bark recording above | CC BY-SA 3.0, adapted from source |

The motion excerpt retains the broadcast's visible FOX Sports watermark and
some event graphics. Cases 03 and 05 explicitly test whether the model can
follow motion while leaving those unrelated details behind. The raw source
files are retained beside the H3-ready derivatives for provenance.
