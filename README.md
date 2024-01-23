# Digitally Controlled Buck Converter with STM32G4 Discovery Kit

This repository provides the necessary code and resources to implement a digitally controlled Buck Converter using the STM32G4 Discovery board. The project aims to showcase the capabilities of the STM32G4 microcontroller series and provide a practical example of a power electronics application. **This project was created as a Diploma thesis for my Intergrated Master's Degree in Computer Science and Engineering in University of Ioannina, Greece.**

## Table of Contents

- [Introduction](#introduction)
- [Hardware Setup](#hardware-setup)
- [Software Setup](#software-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

A Buck Converter is a type of step-down DC-DC converter commonly used in power electronics applications. It efficiently converts a higher DC voltage to a lower DC voltage by controlling the duty cycle of a switching transistor. In this project, we leverage the STM32G4 Discovery Kit to implement a digitally controlled Buck Converter.

The STM32G4 Discovery Kit features an STM32G4 microcontroller, which has powerful analog peripherals and advanced control features suitable for power electronics applications. We utilize the microcontroller's capabilities to control the Buck Converter's duty cycle, measure input/output voltages, and regulate the output voltage.

## Important Notes

- The code provided by Biricha Digital Power LTD is similar, but uses the FMAC embedded preproccessor of the Discovery Kit.

- This code does **NOT** use the FMAC dedicated proccessor embedded in the Discovery Kit. Not using the FMAC proccessor has some minor impact in the 3p3z signal  calculating time (400ns more). 

- The code provided **is preconfigured** for some **predefined** Voltage values (INPUT: 12V - OUTPUT: 5V). If you want to change the I/O Voltage values, you must calculate the right arguments with the use of Biricha Digital Power Tool.

- I used Visual Studio Code Extension **PlatformIO IDE** to edit and load this code to the STM32 board. STM32CubeIDE can also be used for this purpose.

## Hardware Setup

To replicate this project, you will need the following components:

- STM32G4 Discovery board
- Buck Converter module
- Power supply (DC input)
- Load (e.g., resistor or LED)

Connect the components as follows:

1. Connect the input voltage from the power supply to the Buck Converter module's input.
2. Connect the Buck Converter module's output to the load.
3. Connect the ground (GND) of the power supply, Buck Converter module, and STM32G4 Discovery board.

Ensure that the connections are secure and proper precautions are taken when dealing with high voltages.

## Software Setup

To set up the software environment, follow these steps:

1. Clone this repository to your local machine.
2. Install the required software components:
   - [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html): Software for configuring the basic settings and ports for STM32 microcontrollers.
   - [STM32CubeG4](https://www.st.com/en/embedded-software/stm32cubeg4.html): Software package containing the HAL (Hardware Abstraction Layer) drivers for STM32G4 microcontrollers.
   - [Power Supply Design Tool for STM32 - Biricha Digital Power Ltd](https://www.biricha.com/st-wds.html): Software tools and resources for power electronics design and simulation.

## Usage

To use the digitally controlled Buck Converter:

1. Connect the STM32G4 Discovery board to your computer using a USB cable.
2. Flash the compiled binary onto the microcontroller using PlatformIO.
3. Once the program is running on the board, it will start controlling the Buck Converter.
4. Monitor the output voltage and adjust the duty cycle as necessary using the code provided.
5. You can modify the code to implement additional features or customize the behavior of the Buck Converter.

## Contributing

I would like to thank Assistant Prof. mr. [Aristeidis Eythimiou](https://www.cse.uoi.gr/~efthym/Site/Welcome.html)for helping me with the implementation of this project.

## Basic circuit

![](https://lh4.googleusercontent.com/nR79YK-nLXDe47X75F59_lEJoo2Vb4CisIjTSMdLRlHnONetmd9kqCmBopNW-nyRG13CIL10QcnqNKRmfwqCAI-fLAl9ufjY2zrmGDhtIYZ6nzDVB-r9V86wJkjxa57Cq1_0Py7Y4Y6BxMU61fVBCQ)

## License

This project is licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause) by ST Microelectronics. The BSD 3-Clause License is a permissive open source license that allows you to freely use, modify, and distribute the code, both in source and binary forms, for both commercial and non-commercial purposes.

Under the BSD 3-Clause License, you are required to include a copy of the original license and copyright notice in any redistribution or derivative works. However, you are not obligated to share any modifications you make to the code.

Please review the full text of the BSD 3-Clause License for complete details on your rights and obligations.

This code is a modified version of the ST Microelectronics code.

---

We hope this project helps you understand the implementation of a digitally controlled Buck Converter using the STM32G4 Discovery board.
