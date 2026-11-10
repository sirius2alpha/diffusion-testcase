# Case 05: Image, Video, and Audio Role Composition

References, in upload order:

- `../assets/raw/dog_subject.jpg` as `<Picture 1>`: dog identity.
- `../assets/processed/dog_agility_motion_12s.mp4` as `<Video 1>`: motion and camera reference.
- `../assets/processed/dog_bark.wav` as `<Audio 1>`: bark sound reference.

```text
subject_definitions:
<Subject 1> The Papillon dog sourced from <Picture 1>, with a small build, long fringed ears, a mostly white coat, and black markings.
<Video 1> A short agility clip used for movement timing and camera tracking only. Its Border Collie, handler, venue, crowd, watermark, and event graphics must not be copied.
<Audio 1> A short dog-bark recording used as the target diegetic bark sound.
<Picture 1> The supplied agility photograph defines <Subject 1>'s identity only.

summary:
Create an 8-second audiovisual clip combining dog identity from <Picture 1>, agility motion from <Video 1>, and bark sound from <Audio 1>.

retention_analysis:
<Subject 1>: fully_preserved - retain the Papillon's identity and black-and-white appearance while performing a new action.
<Video 1>: attribute_transfer - transfer running, one jump, and tracking rhythm; exclude all source identities and broadcast details.
<Audio 1>: partially_copy - use the bark event and timbre as the dog's diegetic sound.
<Picture 1>: attribute_transfer - transfer dog identity only, not original composition or venue.

detailed_description: [Shot 1] In a simple open grass field, <Subject 1> runs from left to right, makes one clean jump, lands, and turns toward the camera. Follow the motion rhythm and tracking pace of <Video 1>. Place a brief bark from <Audio 1> at the visible turn so the sound and mouth action align. Keep the Papillon from <Picture 1>; do not copy the Border Collie, handler, audience, venue, FOX Sports watermark, or scoreboard. Use one continuous shot.

overall_soundscape: Use <Audio 1> for the brief diegetic bark, with quiet outdoor ambience and soft paw impacts. Exclude commentary and crowd audio.

non_diegetic_music: N/A
```

Primary checks: correct assignment of all three reference roles, cross-modal
timing, identity preservation, and resistance to unintended source copying.
