# TrackAPP - APP Tested on MACBOOK PRO M1
Track Time of the apps that you are using using Python3 with a CLI Interface.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Setup

To run TrackAPP, follow these steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/yourusername/trackapp.git
```


3. Navigate to the project directory:

```
cd trackapp
```


3. Create a virtual environment and activate it:

```
pip install virtualenv
virtualenv env
source env/bin/activate
```


4. Install the required dependencies:

```
pip install psutil 
```


## Usage

1. After setting up the virtual environment and installing dependencies, run the following command to start the application:

```
python3 TrackAPP.py
```


2. The application will open a Command Line Interface (CLI) where you can enter the name of the app you want to track.

3. After entering the name of the app press ``ENTER`` to start tracking the specified app.

4. The app will send notifications when the specified app is opened and closed, along with the duration it was open.

5. To stop the application, press `Ctrl+C` in the terminal where the application is running.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
If you encounter any issues or have questions, feel free to [open an issue](https://github.com/ajdev05/TrackAPP/issues) on this repository.
