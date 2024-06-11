import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw the context diagram (Level 0 DFD)
def draw_context_diagram():
    fig, ax = plt.subplots(figsize=(10, 7))

    # Draw the system boundary
    system_boundary = patches.Rectangle((0.3, 0.3), 0.4, 0.4, linewidth=1.5, edgecolor='black', facecolor='lightgray', label="Branch System")
    ax.add_patch(system_boundary)

    # Draw external entities
    users = patches.Rectangle((0.05, 0.4), 0.2, 0.2, linewidth=1.5, edgecolor='black', facecolor='white')
    credit_bureaus = patches.Rectangle((0.7, 0.7), 0.25, 0.15, linewidth=1.5, edgecolor='black', facecolor='white')
    payment_gateways = patches.Rectangle((0.7, 0.15), 0.25, 0.15, linewidth=1.5, edgecolor='black', facecolor='white')

    ax.add_patch(users)
    ax.add_patch(credit_bureaus)
    ax.add_patch(payment_gateways)

    # Add text
    ax.text(0.1, 0.5, "Users", fontsize=12, ha="center")
    ax.text(0.8, 0.75, "Credit Bureaus", fontsize=12, ha="center")
    ax.text(0.8, 0.2, "Payment Gateways", fontsize=12, ha="center")
    ax.text(0.5, 0.5, "Branch System", fontsize=12, ha="center")

    # Draw arrows for data flow
    ax.arrow(0.25, 0.5, 0.05, 0, head_width=0.03, head_length=0.03, fc='black', ec='black')
    ax.arrow(0.45, 0.5, -0.05, 0, head_width=0.03, head_length=0.03, fc='black', ec='black')

    ax.arrow(0.7, 0.5, -0.05, 0.15, head_width=0.03, head_length=0.03, fc='black', ec='black')
    ax.arrow(0.7, 0.6, -0.05, -0.15, head_width=0.03, head_length=0.03, fc='black', ec='black')

    ax.arrow(0.55, 0.5, 0.05, 0.15, head_width=0.03, head_length=0.03, fc='black', ec='black')
    ax.arrow(0.55, 0.5, 0.05, -0.15, head_width=0.03, head_length=0.03, fc='black', ec='black')

    # Set the limits and hide axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0,0)
