# Case 02: Subject and Scene Disentanglement

References, in upload order:

- `../assets/raw/dog_subject.jpg` as `<Picture 1>`: subject identity.
- `../assets/raw/forest_scene.jpg` as `<Picture 2>`: environment only.

```text
subject_definitions:
<Subject 1> The Papillon dog sourced from <Picture 1>, with a small build, long fringed ears, a mostly white coat, and black markings.
<Subject 2> The forest clearing sourced from <Picture 2>, including its open grassy center and tree line. It defines the environment, not the subject.
<Picture 1> The supplied agility photograph is an identity reference for <Subject 1>; do not preserve its jump pose or venue.
<Picture 2> The supplied forest photograph is an environment reference for <Subject 2>; do not copy any incidental people or objects.

summary:
Create an 8-second audiovisual clip placing <Subject 1> in <Subject 2>. Keep the two reference roles separate.

retention_analysis:
<Subject 1>: fully_preserved - retain the Papillon's identity and black-and-white appearance while changing its pose.
<Subject 2>: partially_preserved - retain the open clearing and forest edge while allowing a new camera composition and lighting.
<Picture 1>: attribute_transfer - transfer dog identity only; exclude agility equipment and the source framing.
<Picture 2>: attribute_transfer - transfer the clearing and tree line only; exclude incidental source details.

detailed_description: [Shot 1] A wide establishing view of a quiet forest clearing based on <Subject 2>. <Subject 1> enters from the left, trots across the grass, pauses near the center, and sniffs the ground. Keep the dog clearly recognizable and separate from the background. Use a slow, level camera pan. Do not add another dog or copy the agility venue from <Picture 1>.

overall_soundscape: Quiet woodland ambience, soft leaves moving in a light breeze, and subtle paw sounds. No speech.

non_diegetic_music: N/A
```

Primary checks: whether the model assigns the dog and environment to the right
references, and whether details from either source image leak across roles.
