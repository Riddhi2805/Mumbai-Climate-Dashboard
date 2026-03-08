import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------- SIDEBAR ----------
st.sidebar.title("🌍 Climate Dashboard")

st.sidebar.markdown("""
### Navigation
Use the menu below to explore the dashboard.
""")


st.title("📁 Analyze Your Own Dataset")

st.write("""
Upload any CSV dataset to explore relationships between variables.
The app automatically generates visualizations, analysis and interpretation.
""")

st.divider()

uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file is not None:

    # ---------- LOAD DATA ----------
    df = pd.read_csv(uploaded_file)

    # Handle missing numeric values
    df = df.fillna(df.mean(numeric_only=True))

    # ---------- DATA PREVIEW ----------
    st.subheader("🔎 Dataset Preview")

    with st.expander("View Dataset"):
        st.dataframe(df.head())

    # ---------- DATASET INFO ----------
    st.subheader("📊 Dataset Information")

    col1, col2 = st.columns(2)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.divider()

    # ---------- NUMERIC VARIABLES ----------
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) < 2:
        st.warning("Dataset must contain at least two numeric variables.")
        st.stop()

    # ---------- SUMMARY STATISTICS ----------
    st.subheader("📈 Summary Statistics")
    st.dataframe(df.describe())

    st.divider()

    # ---------- CORRELATION HEATMAP ----------
    st.subheader("🔗 Correlation Matrix")

    fig, ax = plt.subplots(figsize=(8,5))

    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

    st.divider()

    # ---------- VARIABLE SELECTION ----------
    st.subheader("📉 Compare Two Variables")

    col1, col2 = st.columns(2)

    x_var = col1.selectbox("Select X variable", numeric_cols)
    y_var = col2.selectbox("Select Y variable", numeric_cols)

    # ---------- SCATTER PLOT ----------
    fig2, ax2 = plt.subplots()

    ax2.scatter(df[x_var], df[y_var])

    ax2.set_xlabel(x_var)
    ax2.set_ylabel(y_var)

    ax2.set_title(f"{x_var} vs {y_var}")

    st.pyplot(fig2)

    st.divider()

    # ---------- RELATIONSHIP ANALYSIS ----------
    st.subheader("📊 Relationship Analysis")

    corr = df[x_var].corr(df[y_var])

    if corr > 0.7:
        relation_strength = "a strong positive relationship"
    elif corr > 0.3:
        relation_strength = "a moderate positive relationship"
    elif corr > -0.3:
        relation_strength = "a weak relationship"
    elif corr > -0.7:
        relation_strength = "a moderate negative relationship"
    else:
        relation_strength = "a strong negative relationship"

    st.write(f"""
The relationship between **{x_var}** and **{y_var}** shows **{relation_strength}**.

The correlation coefficient is **{corr:.2f}**.
""")

    st.divider()

    # ---------- CHANGE ANALYSIS ----------
    st.subheader("📈 Change Analysis")

    x_change = df[x_var].iloc[-1] - df[x_var].iloc[0]
    y_change = df[y_var].iloc[-1] - df[y_var].iloc[0]

    st.write(f"""
• **{x_var}** changed by **{x_change:.2f}** from the beginning to the end of the dataset.

• **{y_var}** changed by **{y_change:.2f}** over the same period.
""")

    st.divider()

    # ---------- INTERPRETATION ----------
    st.subheader("📌 Interpretation")

    if corr > 0.3:
        insight = f"As **{x_var}** increases, **{y_var}** also tends to increase."
    elif corr < -0.3:
        insight = f"As **{x_var}** increases, **{y_var}** tends to decrease."
    else:
        insight = f"There is no strong relationship between **{x_var}** and **{y_var}**."

    st.write(f"""
The scatter plot suggests that **{insight}**

This indicates that the two variables may be related and should be considered together
when analyzing the dataset.
""")

    st.divider()

    # ---------- IMPACT ANALYSIS ----------
    st.subheader("⚠ Impact Assessment")

    positive_impacts = []
    negative_impacts = []

    if corr > 0.5:
        positive_impacts.append("Strong positive relationships may help predict one variable using another.")

    if corr < -0.5:
        negative_impacts.append("Strong negative relationships may indicate inverse behavior between variables.")

    if abs(corr) < 0.3:
        negative_impacts.append("Weak relationships indicate that variables may not significantly influence each other.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Potential Insights")
        for p in positive_impacts:
            st.success(p)

    with col2:
        st.subheader("⚠ Potential Concerns")
        for n in negative_impacts:
            st.error(n)

    st.divider()

    # ---------- RECOMMENDATIONS ----------
    st.subheader("💡 Recommendations")

    st.info("""
• Investigate variables with strong correlations for deeper analysis.

• Weak correlations suggest variables behave independently.

• Combining multiple variables in predictive models may reveal stronger patterns.

• Monitoring relationships over time may help detect emerging trends.
""")

    st.success("""
This analysis dynamically updates based on the selected variables,
allowing users to explore relationships within their dataset.
""")