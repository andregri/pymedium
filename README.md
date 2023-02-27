# pymediumapi

<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

**pymediumapi** is a Python3 package to interact with the [API of Medium](https://github.com/Medium/medium-api-docs)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Make sure to have `python3`, `pip` installed.

### Installation

1. Get a free **Integration token** at [https://medium.com/](https://medium.com/) and create an enviroment variable `export MEDIUM_INTEGRATION_TOKEN=<your token>`
2. Clone the repo
   ```sh
   git clone https://github.com/andregri/pymediumapi.git
   ```
3. Create a virtual environment and install requirements
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Example to authenticate and get a list of pubblications you subscribed:

```python
import os
import pymediumapi


def main():
    client = pymediumapi.Client(os.environ.get('MEDIUM_INTEGRATION_TOKEN'))

    try:
        client.authenticate()
    except Exception as e:
        print("Failed authentication: " + str(e))
        quit()

    try:
        pubblications = client.get_pubblications()
    except Exception as e:
        print("Failed get pubblications: " + str(e))
        quit()

    if pubblications:
        pub_id = pubblications[0]["id"]

        try:
            contributors = client.get_contributors(pub_id)
        except Exception as e:
            print("Failed getting contributors: " + str(e))
        else:
            print(contributors)
    else:
        print("There are no pubblications")
        quit()


if __name__ == "__main__":
    main()
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Upload post under pubblications
- [] Upload images
- [] Upload the package

See the [open issues](https://github.com/andregri/pymediumapi/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Andrea Grillo - [@AndreaGrillo96](https://twitter.com/AndreaGrillo96)

Project Link: [https://github.com/andregri/pymediumapi](https://github.com/andregri/pymediumapi)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Medium API Docs](https://github.com/Medium/medium-api-docs)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/andregri/pymediumapi.svg?style=for-the-badge
[contributors-url]: https://github.com/andregri/pymediumapi/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/andregri/pymediumapi.svg?style=for-the-badge
[forks-url]: https://github.com/andregri/pymediumapi/network/members
[stars-shield]: https://img.shields.io/github/stars/andregri/pymediumapi.svg?style=for-the-badge
[stars-url]: https://github.com/andregri/pymediumapi/stargazers
[issues-shield]: https://img.shields.io/github/issues/andregri/pymediumapi.svg?style=for-the-badge
[issues-url]: https://github.com/andregri/pymediumapi/issues
[license-shield]: https://img.shields.io/github/license/andregri/pymediumapi.svg?style=for-the-badge
[license-url]: https://github.com/andregri/pymediumapi/blob/master/LICENSE.md
