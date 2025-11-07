# Midterm Project: Predicting Antibiotic-Producing Bacteria Using Morphological Features

## Problem Statement

Antibiotic resistance represents one of the most pressing global health challenges of our time. While bacteria are known to produce secondary metabolites that can be repurposed as novel antibiotics, the traditional discovery pipeline for these compounds is inefficient and time-consuming, with success rates declining significantly over recent decades.

## Proposed Solution

This project explores a modern approach that combines **image analysis and machine learning** to predict which bacterial strains are most likely to produce bioactive secondary metabolites with antibiotic potential. By analyzing morphological features extracted from bacterial colony images, we can identify promising candidates for further laboratory screening, significantly reducing the time and cost of antibiotic discovery.

## Dataset Description

The dataset contains **morphological features** extracted from bacterial colony images across multiple screening rounds. Each bacterial strain has been experimentally tested for antimicrobial activity against pathogenic bacteria.

**Key features:**
- **Morphological descriptors**: Shape, size, texture, and color characteristics of bacterial colonies
- **Target variable**: `activity_total` - Binary indicator (0/1) of whether the strain exhibits antimicrobial activity

## Project Goal

Build a classification model to predict whether a bacterial strain will exhibit antimicrobial activity based solely on its morphological features, achieving the best possible **AUC score** on validation data.

## Running

### Without Docker 
To run the model
`uv run prediction.py`

To run new prediction
`uv run input.py`

To free port
`lsof -i :Port`
`kill -9 PID`

### With Docker
1. Build
`docker build -t bacteria-predictor .`
2. Run
`docker run --rm -p 9696:9696 bacteria-predictor`
`python input.py`

