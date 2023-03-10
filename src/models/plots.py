import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def plot_data_split(train_data: pd.DataFrame, test_data: pd.DataFrame) -> go.Figure:
    """Plot time series data split.

    Args:
        train_data: Data used for model training.
        test_data: Data used for model testing.

    Returns:
        Plotly figure.
    """
    return go.Figure(
        [
            go.Scatter(
                name="Training",
                x=train_data.index,
                y=train_data["Adj Close"],
                mode="lines",
            ),
            go.Scatter(
                name="Testing",
                x=test_data.index,
                y=test_data["Adj Close"],
                mode="lines",
            ),
        ]
    ).update_layout(
        yaxis_title="Adj. Close price",
        xaxis_title="Date",
        legend_title="Data",
    )


@st.cache_data(show_spinner="Plotting train and test sets...")
def plot_data_split_st_cached(*args, **kwargs) -> go.Figure:
    return plot_data_split(*args, **kwargs)


def plot_data_predictions(test_data: pd.DataFrame, pred: pd.Series) -> go.Figure:
    """Plot training, testing and predicted data.

    Args:
        train_data: Data used for model training.
        test_data: Data used for model testing.
        pred: Predicted data.

    Returns:
        Plotly figure.
    """
    return go.Figure(
        [
            go.Scatter(
                name="Testing",
                x=test_data.index,
                y=test_data["Adj Close"],
                mode="lines",
            ),
            go.Scatter(
                name="Predicted",
                x=pred.index,
                y=pred,
                mode="lines",
            ),
        ]
    ).update_layout(
        yaxis_title="Adj. Close price",
        xaxis_title="Date",
        legend_title="Data",
    )


@st.cache_data(show_spinner="Plotting train and test sets...")
def plot_data_predictions_st_cached(*args, **kwargs) -> go.Figure:
    return plot_data_predictions(*args, **kwargs)
