import streamlit as st

# Título de la aplicación
st.title('Calculadora de Balance de Masa para Pulpa')
st.write('Resuelve el problema de balance de masa de pulpa que se muestra en la imagen.')

# Sección para la entrada de datos del usuario
st.header('Entrada de Datos')
st.markdown('---')

# M1 - Pulpa Inicial
st.subheader('Pulpa Inicial')
m1 = st.number_input('Masa de la Pulpa Inicial (kg)', value=50.0, step=0.1, format="%.2f")
st.info('El valor de la pulpa inicial (M1) es de 50 kg, según el enunciado del problema.')

# X1 - Sólidos Solubles en la Pulpa Inicial
st.subheader('Concentración de Sólidos Solubles (Azúcar)')
x1 = st.number_input('Concentración de Azúcar en la Pulpa Inicial (%)', value=7.0, step=0.1, format="%.2f")
st.info('La concentración de sólidos solubles (azúcar) en la pulpa inicial (X1) es de 7%, según el enunciado del problema.')

# X3 - Grados Brix deseados en la Pulpa Final
x3 = st.number_input('Concentración de Azúcar Deseada (%)', value=10.0, step=0.1, format="%.2f")
st.info('La concentración de azúcar deseada en la pulpa final (X3) es de 10%, según el enunciado del problema.')

# Sección de resultados
st.header('Resultados del Balance de Masa')
st.markdown('---')

# Convertir porcentajes a fracciones
x1_frac = x1 / 100
x3_frac = x3 / 100

# Calcular M3 - Masa de la Pulpa Final
try:
    if x3_frac > 0:
        m3 = (m1 * x1_frac) / x3_frac
        st.success(f'**Masa de la Pulpa Final (M3):** {m3:.2f} kg')
    else:
        m3 = 0
        st.error('La concentración deseada no puede ser cero.')
except ZeroDivisionError:
    st.error('La concentración deseada no puede ser cero.')
    m3 = 0

# Calcular M2 - Masa del Azúcar a Agregar
m2 = m3 - m1
st.success(f'**Masa de Azúcar a Agregar (M2):** {m2:.2f} kg')

st.markdown('---')
st.info('El balance de masa se realiza con las siguientes ecuaciones:\n\n'
        '**Balance General:** $M_1 + M_2 = M_3$\n\n'
        '**Balance de Sólidos Solubles:** $M_1 X_1 + M_2 X_2 = M_3 X_3$\n\n'
        'Donde $X_2 = 1$ (100% azúcar) y $X_1$ y $X_3$ son las concentraciones en fracción.')
