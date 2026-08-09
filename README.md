# TF-IDF-Based Contribution Framework for Team Science

This repository provides code implementing the TF-IDF-based contribution framework introduced in:

**Xiao, T. (2026). "Who did what? A TF-IDF-based contribution metric for team science." *Journal of Informetrics*.**  

The repository includes the implementation of the framework, example data for the illustrative examples presented in Section 3.1.2 of the paper, and supporting documentation for running the code.

For the conceptual framework, formal definitions, and interpretation of the measures, please refer to the paper.

## Repository Contents

The repository contains:

- Code implementing the TF-IDF-based contribution framework.
- Example data corresponding to the illustrative examples in Section 3.1.2 of the paper.
- Code for reproducing the TF-IDF-based contribution measures for the illustrative examples.
- Information on software dependencies and instructions for running the code.

The repository is organized as follows:

```text
.
├── [tfidf_example.py]
├── [example_data.csv]
├── [requirements.txt]
└── README.md
```

## Requirements

The code was developed using:

- Python 3
- NumPy
- pandas

The required Python packages are listed in `requirements.txt`.

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Running the Code

After installing the required dependencies, run:

```bash
python [tfidf_example.py]
```

The script reads the example contribution data and calculates the corresponding TF-IDF-based contribution measures.

The included example data reproduce the two hypothetical team configurations presented in Section 3.1.2 of the paper.

## Example Data

The example data are hypothetical and are provided solely to illustrate the implementation of the TF-IDF-based contribution framework.

The input data identify, at minimum:

- the team or paper;
- the author;
- the contributor role; and
- whether the author performed the role.

The example data can also be used as a template for applying the code to other structured author-role contribution data.

## License

This project is licensed under the MIT License.
