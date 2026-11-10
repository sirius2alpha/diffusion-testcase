# Case 03: Image Identity with Video Motion Reference

References, in upload order:

- `../assets/raw/dog_subject.jpg` as `<Picture 1>`: dog identity.
- `../assets/processed/dog_agility_motion_12s.mp4` as `<Video 1>`: agility motion and camera movement.

```text
subject_definitions:
<Subject 1> The Papillon dog sourced from <Picture 1>, with a small build, long fringed ears, a mostly white coat, and black markings.
<Video 1> A 12-second agility clip used only for the dog's running, jumping, turning, and weave-pole motion rhythm, plus the tracking camera movement. It also contains a handler, audience, broadcast watermark, and event graphics that are not target content.
<Picture 1> The supplied agility photograph defines <Subject 1>'s identity, not its original pose or venue.

summary:
Create an 8-second audiovisual clip of <Subject 1> performing a short agility run. Use <Video 1> for motion timing and camera behavior while retaining the image subject.

retention_analysis:
<Subject 1>: fully_preserved - retain the Papillon's breed and coat pattern while transferring a new action.
<Video 1>: attribute_transfer - transfer running, turns, jump timing, weave rhythm, and camera tracking; exclude the Border Collie's appearance, handler, venue, crowd, logos, and scoreboard.
<Picture 1>: attribute_transfer - transfer dog identity only.

detailed_description: [Shot 1] In a clean grassy training field with simple low obstacles, <Subject 1> accelerates, makes one low jump, then weaves briefly between two poles. Borrow the quick changes of direction and smooth tracking pace from <Video 1>, but keep the Papillon from <Picture 1>. Use one continuous side-tracking shot. Do not reproduce the source venue, handler, crowd, score graphics, watermark, or Border Collie.

overall_soundscape: Soft paws on grass and light outdoor ambience. No broadcast commentary or crowd noise from <Video 1>; no speech.

non_diegetic_music: N/A
```

Primary checks: identity-motion disentanglement, motion adherence, and leakage
of the source video's handler, venue, graphics, or watermark.
