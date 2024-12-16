# VirSieve

*The reward for doing good is the opportunity to do more. -Jonas Salk*

*The reward for a good deed is another good deed. -Ben Azai.*

The VirSieve pipeline began with the realization that the bioinformatic analysis of viral strains in wastewater
might bioinformatically resemble the bioinformatics of analyzing intratumoral heterogeniety from formalin-fixed
paraffin-embedded tissues.  We hope our approach will prove to be a useful tool for the analysis and surveillance
of emerging and established viral variants using wastewater-based epidemiology.

### Announcements
We are sponsoring a wastewater-based epidemiology symposium in January 2025. [Click here to register](https://www.wastewateramr2025.com/)
)
## [Microbes in Wastewater](https://www.wastewateramr2025.com/) 
### Antibiotic Resistance, Public Health, and Climate Change 
#### January 16-17, 2025 | Newport Beach, California 

### Publication
This pipeline is still underdevelopment and testing, but will remain open-source and will always invite community
participation and feedback.  If you have any questions or suggestions (or a desire to collaborate), please email **mweinstein @t zymoresearch .com**.

## Quick Start Guide

### From a fresh Ubuntu installation where you have admin (sudo) privileges
```bash
sudo apt update
sudo apt install git
sudo apt install docker.io
sudo gpasswd -a $USER docker
git clone --recursive https://github.com/Zymo-Research/VirSieve.git
cd VirSieve
python3 containerBuild.py # This command will build the containers. It and all commands above only need to be run once per system as part of the setup.
python3 runPipeline.py /path/to/working/directory  # This command will also be used to initiate subsequent analyses on new data
```

### Prerequisites

This software should be able to run on nearly any system with Docker installed on an account with sufficient
privileges to run Docker containers.  Having Git on the system will help with recursively cloning the 
relevant submodules and keeping the pipeline up to date, but the code can always be manually copied from 
Github.  The Python code run outside the container (to build the containers and then run them) is intentionally
kept simple and should be compatible with any currently-supported version of Python along with several versions
long since deprecated.

### Installation

All but the last line of the code given above is part of the installation process and should only need to be run one 
time per system.  If Docker and Git are already present on the system, the first three lines can be skipped. Additionally,
if Docker is already present and running on the system, the user is likely to already have permission to run Docker containers
without having to SUDO.  If so, the fourth line can be skipped as well (this can be tested by running `docker container run hello-world`).

### Usage

To run the pipeline, simply use the following command:
```bash
python3 runPipeline.py /path/to/working/directory
```
The working directory will be expected to have the following structure for the pipeline to run automatically:
```
.
+-- workingDirecctoryName
|  +-- rawFASTQ
|     +-- reads-pe1.fastq
|     +-- reads-pe2.fastq
|     +-- adapters.fa
|     +-- primers.bed
```
The adapters.fa and primers.bed files should have those exact names in those exact cases.  The primer file
should be a BED-formatted file containing the primer binding intervals within the genome for use in the iVar 
portion of the pipeline to trim the primers.  The adapters.fa file should be a FASTA-formatted file
containing the adapter sequences to be trimmed from the reads.  The forward- and reverse-read FASTQ files 
can have any name, but they will be expected to follow the Illumina standard of using underscores as a delimiter
with the first field being the sample name (if you have underscores within your sample names, they will likely
be truncated).  There should only be two FASTQ files present and they should end in some appropriate file extension
to identify them as such.

## Outputs of Note

THis pipeline will retain all intermediate files for traceability and diagnostic purposes.  The folders created within
the working directory will give a clue as to the source of the files contained within.  The freyjaOutput folder will
contain data relevant to Freyja as well as the result of the demixing of the sample.  The vepOutputs folder will have
the reported variants along with their expected consequences.  The filteredVCF folder will have the VCF that went
through filtering in GATK for different attributes affecting variant confidence.  By default, only variants with 1% or
greater abundance will be reported.  The BQSR BAM file will contain all of the aligned reads with recalibrated
base quality scores that was used for variant calling while the Mutect2-generated BAM file showing any realignments at
active sites (which can be found in the rawVCF folder) will contain the read data as seen by Mutect2 from de novo 
reassembly around active sites.

## Contributing

We welcome and encourage contributions to this project from the community and will happily accept and acknowledge input (and possibly provide some free kits as a thank you).  We aim to provide a positive and inclusive environment for contributors that is free of any harassment or excessively harsh criticism. Our Golden Rule: *Treat others as you would like to be treated*.

## Versioning

We use a modification of [Semantic Versioning](https://semvar.org) to identify our releases.

Release identifiers will be *major.minor.patch*

Major release: Newly required parameter or other change that is not entirely backwards compatible
Minor release: New optional parameter
Patch release: No changes to parameters

## Authors

- **Michael M. Weinstein** - *Project Lead, Programming and Design* - [michael-weinstein](https://github.com/michael-weinstein)

## License

This project is still in development, but we expect to keep it fully open-source with minimal restrictions on usage.

## Acknowledgments

We would like to thank the following, without whom this would not have happened:
* The Python Foundation
* The staff at Zymo Research
* Our customers

---------------------------------------------------------------------------------------------------------------------

#### If you like this software, please let us know at info@zymoresearch.com.
#### For kits and reagents to assist in your environmental sampling and analysis, please check out [our environmental research offerings](https://www.zymoresearch.com/pages/environmental-research)
#### For full service wastewater analysis, please check out our offerings at [Zymo Environ Wastewater Testing Service](https://www.zymoresearch.com/pages/zymo-environ-covid-19-wastewater-testing-service)
