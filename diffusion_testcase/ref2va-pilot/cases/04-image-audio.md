# Case 04: Image with Audio Reference

References, in upload order:

- `../assets/raw/dog_subject.jpg` as `<Picture 1>`: dog identity.
- `../assets/processed/dog_bark.wav` as `<Audio 1>`: bark sound reference.

```text
subject_definitions:
<Subject 1> The Papillon dog sourced from <Picture 1>, with a small build, long fringed ears, a mostly white coat, and black markings.
<Audio 1> A short recording of a dog barking. Use it as the diegetic bark reference; do not add speech or music.
<Picture 1> The supplied agility photograph defines the dog's identity only.

summary:
Create a 6-second audiovisual clip in which <Subject 1> reacts to a nearby sound and gives a brief bark guided by <Audio 1>.

retention_analysis:
<Subject 1>: fully_preserved - retain the dog's recognizable appearance while changing pose and expression.
<Picture 1>: attribute_transfer - transfer identity only; omit the handler, jump bar, venue, and source composition.
<Audio 1>: partially_copy - use the bark event and acoustic character as the target's diegetic sound without adding unrelated audio.

detailed_description: [Shot 1] A medium shot of <Subject 1> standing in a quiet grassy clearing. The dog turns toward an off-screen sound, opens its mouth, and gives a brief natural bark guided by <Audio 1>, then settles and looks toward the camera. Keep the mouth movement visibly tied to the bark. Do not show another animal or copy the agility setting from <Picture 1>.

overall_soundscape: Use the short dog-bark reference <Audio 1> as the central diegetic event, with faint outdoor ambience and soft paw movement. No speech.

non_diegetic_music: N/A
```

Primary checks: whether the sound is used in the visible scene, whether the
visible action aligns with it, and whether the dog's identity remains stable.
