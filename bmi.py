{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sBzzDUQX-cbX"
      },
      "source": [
        "<font size=\"+3\">Module 48 - BMI App</font>\n",
        "\n",
        "## Context: Understanding the Problem Statement --------Problem Scoping\n",
        "\n",
        "#### BMI Calculator\n",
        "\n",
        "Body Mass Index (BMI) is generally used to broadly categorize a person as underweight, normal weight, overweight, or obese based on their height and weight.\n",
        "For calculating the BMI, we need to know the Weight (in Kg) and Height (in metre) ."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "m5NdTvSl-cbg"
      },
      "source": [
        "#### Import the Streamlit Library"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "04r0XBZr-cbi",
        "outputId": "34346928-65e0-4500-bec5-c2941b56e65f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 330
        }
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'streamlit'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-1aa3dc4fa683>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import streamlit as st"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1d04kroC-cbr"
      },
      "source": [
        "#### Give title to the application and ask user for entering height and weight for calculating BMI"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BPHT0fVH-cbs",
        "outputId": "7cdb3d90-fc05-458e-e69e-fe49f3a71d2d"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2022-09-19 22:36:05.727 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run d:\\my internships\\sustainable living labs\\openvino_env\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ],
      "source": [
        "# give a title to our app\n",
        "st.title('Welcome to BMI Calculator')\n",
        "\n",
        "# TAKE WEIGHT INPUT in kgs\n",
        "weight = st.number_input(\"Enter your weight (in kgs)\")\n",
        "\n",
        "# TAKE HEIGHT INPUT\n",
        "# radio button to choose height format\n",
        "status = st.radio('Select your height format: ',\n",
        "                  ('cms', 'meters', 'feet'))\n",
        "\n",
        "# compare status value\n",
        "if(status == 'cms'):\n",
        "    # take height input in centimeters\n",
        "    height = st.number_input('Enter your height in Centimeters')\n",
        "\n",
        "    try:\n",
        "        bmi = weight / ((height/100)**2)\n",
        "    except:\n",
        "        st.text(\"Enter some value of height\")\n",
        "\n",
        "elif(status == 'meters'):\n",
        "    # take height input in meters\n",
        "    height = st.number_input('Enter your height in Meters')\n",
        "\n",
        "    try:\n",
        "        bmi = weight / (height ** 2)\n",
        "    except:\n",
        "        st.text(\"Enter some value of height\")\n",
        "\n",
        "else:\n",
        "    # take height input in feet\n",
        "    height = st.number_input('Enter your height in Feet')\n",
        "\n",
        "    # 1 meter = 3.28\n",
        "    try:\n",
        "        bmi = weight / (((height/3.28))**2)\n",
        "    except:\n",
        "        st.text(\"Enter some value of height\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t90Fws7C-cbv"
      },
      "source": [
        "#### Classify the BMI index of the person based on the WHO chart"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kxgJgqKG-cbv"
      },
      "source": [
        "![who_chart.jpg](attachment:who_chart.jpg)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "K5u-pkVI-cbw"
      },
      "outputs": [],
      "source": [
        "# check if the button is pressed or not\n",
        "if(st.button('Calculate BMI')):\n",
        "\n",
        "    # print the BMI INDEX\n",
        "    st.text(\"Your BMI Index is {}.\".format(bmi))\n",
        "\n",
        "    # give the interpretation of BMI index\n",
        "    if(bmi < 16):\n",
        "        st.error(\"You are Extremely Underweight\")\n",
        "    elif(bmi >= 16 and bmi < 18.5):\n",
        "        st.warning(\"You are Underweight\")\n",
        "    elif(bmi >= 18.5 and bmi < 25):\n",
        "        st.success(\"Healthy\")\n",
        "    elif(bmi >= 25 and bmi < 30):\n",
        "        st.warning(\"Overweight\")\n",
        "    elif(bmi >= 30):\n",
        "        st.error(\"Extremely Overweight\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uzoK4oWt-cb1"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.5"
    },
    "toc": {
      "base_numbering": 1,
      "nav_menu": {},
      "number_sections": false,
      "sideBar": true,
      "skip_h1_title": false,
      "title_cell": "Table of Contents",
      "title_sidebar": "Contents",
      "toc_cell": false,
      "toc_position": {},
      "toc_section_display": true,
      "toc_window_display": true
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
