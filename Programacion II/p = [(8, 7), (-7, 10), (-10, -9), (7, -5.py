p = [(8, 7), (-7, 10), (-10, -9), (7, -5)]

# Cálculo de pendientes
def m(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0]) if (p2[0] - p1[0]) != 0 else float('inf')

m_AB = m(p[0], p[1])
m_BC = m(p[1], p[2])
m_CD = m(p[2], p[3])
m_DA = m(p[3], p[0])

# Evaluación
es_trapecio = (m_AB == m_CD) or (m_BC == m_DA)

print(f"Pendientes: AB={m_AB}, BC={m_BC}, CD={m_CD}, DA={m_DA}")
print(f"¿Es trapecio?: {es_trapecio}")