# Social Content Delivery MongoDB setup

Use a development MongoDB instance or an Atlas development cluster. In PowerShell, run these commands from the project root.

```powershell
python -m pip install -r deliverables/requirements-mongodb.txt
$env:MONGODB_URI = 'mongodb://localhost:27017'
python deliverables/mongodb_setup.py
```

For Atlas, use your cluster connection string in `MONGODB_URI`. Set `MONGODB_DB` to select another database. The default is `social_content_dev`.

To populate an approved development database with the project’s existing Vajra Global knowledge files, run:

```powershell
python deliverables/mongodb_setup.py --knowledge-dir knowledge-layer-draft
```

The import seeds the client and LinkedIn project, then saves the five source files as draft knowledge versions. Repeating the import with the same source content preserves existing documents. Changed source content creates a new draft version. Knowledge approval is a separate step.

Pass `--include-delivery` to also initialize `publications` and `performanceSnapshots`. The setup creates collections and indexes. Application endpoints, client authorization, and workflow writes are separate implementation steps.
