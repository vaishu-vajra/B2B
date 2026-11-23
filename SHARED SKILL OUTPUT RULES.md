# Shared Skill Output Rules

Use these rules for every skill created or run for this project.

## Save locations

- Save every skill result in the project-root `output` folder.
- Save each Context Assembler package in the project-root `context package` folder. Create a separate package for each workflow stage; do not reuse another stage’s package.
- Keep the skill result and its context package as separate files.

## File names

- Name a skill result `<skill_name>_<MM>_<DD>_<version>.md`, using a readable skill name with spaces replaced by underscores. Start with version `01` for each skill on a date and increment it for additional runs. Example: `brief_qualifier_11_12_01.md`.
- Name a context package `context_assembler_<MM>_<DD>_<version>_<stage_name>.md`, using a readable lowercase stage name with underscores. Example: `context_assembler_11_12_01_brief_qualifier.md`.
- If the same skill or stage is run more than once on the same date, add a version suffix such as `_v2`, `_v3` to the later file. Do not overwrite an earlier run.

## Skill instructions

- Every skill’s `SKILL.md` must follow these shared save locations and naming rules, while keeping that skill’s own required content and output structure.
- When creating or updating a skill, include these rules in its instructions or state that it follows this shared project standard.
- Use the actual skill output and actual context package in the files. Do not substitute links, document pointers, or coded references for the content.

## Run authenticity

- Save a skill output only when it is the actual result of running that skill. Do not write, reconstruct, or paraphrase a substitute report.
- Save a context package only when it is the actual result of running Context Assembler for that specific workflow stage and run. Do not write or reuse a substitute package.
- If the skill cannot be run, do not create an output or context package. Explain the limitation and leave the files unsaved.

## Latest run logs

- In addition to the dated canonical files in `context package/` and `output/`, copy each actual Context Assembler package into the project-root `context_package_latest/` folder and each actual skill output into the project-root `output_latest/` folder.
- These folders are append-only run logs. Keep the original dated filenames, include each new actual run, and never overwrite an earlier run. Copy only genuine outputs from that run; do not create summaries or substitute files in their place.
- For a stage run, place its Context Assembler package in `context_package_latest/` and its corresponding skill output in `output_latest/`. Continue saving the canonical files in their existing folders too.
- The current Brief Qualifier run history has been copied into these folders as runs 01, 02, and 03. Apply this rule to subsequent skills and future skills created for the project.

## Workflow-stage ownership

- Brief Qualifier, Content Planner, Post Writer, and Post Quality Analyst report only their own stage decisions and any human approval state explicitly supplied for that stage. Do not add statements that an approval does not authorize publication, mark publication approval pending, or assess account access, publishing credentials, live-post status, or publication verification in these stages.
- The designated human approver approves the entire calendar version once. After explicit approval of all posts on that version, Post Writer drafts the whole calendar in order. Partial approval holds the whole batch. Show calendar approval once and use item status only for brief completeness.
- Content Planner may assign proposed calendar dates and deadlines because they are planning fields. Keep them separate from actual publication status.
- Publish and Verify owns the final-copy approval check, publisher access check, publication action, live-post verification, and publication record. Its instructions are the sole source for those checks.
- Preserve human review and approval states needed for workflow handoffs; do not infer approval from a stage verdict.