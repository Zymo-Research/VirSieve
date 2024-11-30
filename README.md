Will expand on this in the future.

**Container build** will trigger the building and appropriate tagging of the required containers if the submodules are all downloaded.
To get all the submodules, run the following command:

```bash
git clone --recursive https://github.com/Zymo-Research/VirSieveAlign.git
```

**Run pipeline** will trigger the pipeline to run against a folder.  To start off, the folder should contain a subfolder called *rawFASTQ* containing a set of paired forward and reverse read files.  It should also contain an adapters.fa FASTA file containing the adapter sequences to be trimmed and a primers.bed file describing the locations of the primers used to generate the amplicon library.
