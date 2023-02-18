<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Leynia/PainGenerator/blob/main/resources/PAIN.png">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">PainGenerator</h3>

  <p align="center">
    A small Python program to generate textures based on the video game Cruelty Squad
    <br />
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
      </ul>
    </li>
    <li>
      <a href="#options">Options</a>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Pain Generator][product-screenshot]

Created by Leia
</br>
Original textures and concept from Cruelty Squad by Ville Kallio, Consummer Softproducts
</br>
</br>
Pain Generator is a small python program which allows you to generate random images in the style of the 'PUNISHMENT' texture from the Cruelty Squad level MALL MADNESS,
there is also the option for the texture to be generated based on user input.
</br>
I learned Python with this project which is why the code is badly written, mismatched, and probably not very efficient ;).
</br>
</br>
This page is just an easy way to get the source code in case you'd like to tinker with the program and run it in your own python environment, for a fully functional .exe with no requirements needed, head to [https://crus.cc/mod/pain_generator/](https://crus.cc/mod/pain_generator/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Requirements

* A python environment
</br>
Packages:
* Pillow
* NLTK
* PySimpleGUI

## Options

Random/User Generated Checkbox = Switch between random or user input-based generation.
</br>
</br>
[User input-based mode] Word = Word you'd like to have on the texture
</br>
</br>
[User input-based mode] Hex Value 1, 2, Reset Hex = The color you would like to have as a gradient on the texture, must be in HEX value (Example : White = #FFFFFF), Reset Hex button resets to the basic program values (Red and Blue)
</br>
</br>
[Random mode] How many images would you like to generate = The number of image you would like to be randomly generated. 1 -> 100
</br>
</br>
[Random mode] Wordlist = This program has three built in wordlists, "Cyberpunk AF" is a wordlist based upon William Gibson's "SPRAWL" trilogy of books. "TempleOS" is based upon the OS and writings of Terry A. Davis. "1894" is based upon the classic book "1984" by George Orwell.
</br>
</br>
The lists have been carefully crafted but are large ('Cyberpunk AF' = ~21000 words, 'TempleOS' = ~7000 words, '1894' = ~7000 words), they are not supposed to contain any words which may be interpreted as offensive to any group, but if you find one, please contact me on Discord.
</br>
</br>
Output Folder = where you would like the images to be saved. Default folder is the "Results" folder bundled along with the software.
</br>
</br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under The Unlicense license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Twitter - [@LeiaIsOnline](https://twitter.com/LeiaIsOnline)
</br>
Discord - Leia#4939

Project Link: [https://github.com/Leynia/PainGenerator](https://github.com/Leynia/PainGenerator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: https://crus.cc/mod/pain_generator/image.jpg
