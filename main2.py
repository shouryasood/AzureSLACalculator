import tkinter as tk
from tkinter import ttk

class CompositeSLACalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AZURE - SLA Calculator")

        self.component_slas = {
            "Azure DNS": 100,
            "Cosmos DB": 99.999,
            "Redis Cache": 99.995,
            "SQL Database": 99.995,
            "Event Hubs": 99.99,
            "Virtual Machines": 99.99,
            "Database for PostgreSQL": 99.99,
            "Microsoft Entra ID": 99.99,
            "API Management": 99.99,
            "Azure Comms. Gateway": 99.99,
            "Azure Front Door": 99.99,
            "Azure Storage": 99.99,
            "Apache Cassandra MI": 99.99,
            "Azure AD EI": 99.99,
            "Event Grid": 99.99,
            "Private Link": 99.99,
            "Azure NetApp Files": 99.99,
            "Database for MySQL": 99.99,
            "Azure Key Vault": 99.99,
            "Azure Firewall": 99.99,
            "Database for MariaDB": 99.99,
            "DDoS Protection": 99.99,
            "Load Balancer": 99.99,
            "Traffic Manager": 99.99,
            "Databricks": 99.95,
            "Kubernetes Service": 99.95,
            "Route Server": 99.95,
            "Container Apps": 99.95,
            "Azure Bastion": 99.95,
            "App Service": 99.95,
            "Application Gateway": 99.95,
            "Azure Functions": 99.95,
            "VPN Gateway": 99.95,
            "Azure Red Hat OpenShift": 99.95,
            "Virtual WAN": 99.95,
            "Cloud Services": 99.95,
            "ExpressRoute": 99.95,
            "Azure AI Search": 99.9,
            "Operator Insights": 99.9,
            "Azure VMware Solution": 99.9,
            "SQL Server Stretch DB": 99.9,
            "Azure Chaos Studio": 99.9,
            "Microsoft Entra DS": 99.9,
            "Remote Rendering": 99.9,
            "Service Bus": 99.9,
            "Azure Arc": 99.9,
            "Comm. Services": 99.9,
            "Site Recovery": 99.9,
            "VNet Manager": 99.9,
            "Confidential Ledger": 99.9,
            "Cognitive Services": 99.9,
            "Azure Purview": 99.9,
            "Container Instances": 99.9,
            "Microsoft Dev Box": 99.9,
            "Defender for Cloud": 99.9,
            "Digital Twins": 99.9,
            "Energy Data Manager": 99.9,
            "Azure Monitor": 99.9,
            "Media Services": 99.9,
            "Network Watcher": 99.9,
            "Data Share": 99.9,
            "Applied AI Services": 99.9,
            "Synapse Analytics": 99.9,
            "Container Registry": 99.9,
            "Load Testing": 99.9,
            "Microsoft Sentinel": 99.9,
            "Spatial Anchors": 99.9,
            "Health Data Services": 99.9,
            "Automation": 99.9,
            "Azure CDN": 99.9,
            "StorSimple": 99.9,
            "Machine Learning": 99.9,
            "Data Explorer": 99.9,
            "Azure Batch": 99.9,
            "Managed Grafana": 99.9,
            "Information Protection": 99.9,
            "IoT Central": 99.9,
            "Web PubSub": 99.9,
            "Azure Backup": 99.9,
            "Data Lake Storage": 99.9,
            "Bot Service": 99.9,
            "Data Factory": 99.9,
            "Azure DevOps": 99.9,
            "Azure Maps": 99.9,
            "Notification Hubs": 99.9,
            "Microsoft Genomics": 99.9,
            "Power BI Embedded": 99.9,
            "Azure Spring Apps": 99.9,
            "IoT Hub": 99.9,
            "Logic Apps": 99.9,
            "Analysis Services": 99.9,
            "App Configuration": 99.9,
            "Time Series Insights": 99.9,
            "Data Lake Analytics": 99.9,
            "Lab Services": 99.9,
            "Data Catalog": 99.9,
            "SignalR Service": 99.9,
            "HDInsight": 99.9,
            "Visual Studio App Center": 99.9,
            "Stream Analytics": 99.9,
            "Open Datasets": 0.0,
            "Microsoft Fabric": 0.0,
            "Service Fabric": 0.0,
            "DevTest Labs": 0.0,
            "Dedicated HSM": 0.0,
            "IoT Edge": 0.0,
            "Azure Advisor": 0.0,
            "Azure Migrate": 0.0,
            "Virtual Network": 0.0,
            "Managed Disks": 0.0,
            "Project Bonsai": 0.0,
            "HDInsight on AKS": 0.0,
            "VM Scale Sets": 0.0,
            "Deployment Environments": 0.0,
            "Azure Sphere": 0.0,
            "Azure Blueprints": 0.0,
            "DB Migration Service": 0.0,
            "Azure Orbital": 0.0,
            "Avere vFXT": 0.0,
            "CycleCloud": 0.0,
            "Object Anchors": 0.0,
            "Cost Management": 0.0,
            "Data Box": 0.0,
            "Internet Analyzer": 0.0,
            "HPC Cache": 0.0,
            "Virtual Desktop": 0.0,
            "Defender for IoT": 0.0,
            "Azure Policy": 0.0,
            "Resource Mover": 0.0,
            "Azure Elastic SAN": 0.0,
            "Dedicated Host": 0.0,
            "Managed Apps": 0.0,
            "Managed Lustre": 0.0,
            "Azure Quantum": 0.0,
            "Cloud Shell": 0.0,
            "Azure Portal": 0.0,
            "Azure Lighthouse": 0.0,
            "Azure Automanage": 0.0,
            "Kubernetes Fleet Manager": 0.0,
            "Copilot in Azure": 0.0
        }


        self.selected_services = []

        self.create_widgets()

    def create_widgets(self):
        # Service dropdown
        service_label = ttk.Label(self, text="Select Azure Service:")
        self.service_var = tk.StringVar()
        service_dropdown = ttk.Combobox(self, textvariable=self.service_var, values=list(self.component_slas.keys()))
        service_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        service_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        # Delete Service button
        delete_button = ttk.Button(self, text="Delete Service", command=self.delete_service)
        delete_button.grid(row=7, column=0, columnspan=2, pady=10)

        # SLA entry
        sla_label = ttk.Label(self, text="SLA (%):")
        self.sla_var = tk.StringVar()
        sla_entry = ttk.Entry(self, textvariable=self.sla_var)
        sla_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        sla_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Add Service button
        add_button = ttk.Button(self, text="Add Service", command=self.add_service)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Calculate button
        calculate_button = ttk.Button(self, text="Calculate", command=self.calculate_sla)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Treeview for displaying added services
        columns = ("Service", "SLA (%)")
        self.services_tree = ttk.Treeview(self, columns=columns, show="headings", selectmode="browse")

        for col in columns:
            self.services_tree.heading(col, text=col)

        self.services_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        # Result labels
        result_label1 = ttk.Label(self, text="Composite SLA:")
        result_label1.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

        self.result_var1 = tk.StringVar()
        result_value1 = ttk.Label(self, textvariable=self.result_var1)
        result_value1.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        result_label2 = ttk.Label(self, text="Probability of Failure:")
        result_label2.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

        self.result_var2 = tk.StringVar()
        result_value2 = ttk.Label(self, textvariable=self.result_var2)
        result_value2.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        # Bind function to update SLA on selection change
        service_dropdown.bind("<<ComboboxSelected>>", self.update_selected_sla)

        # Downtime labels
        downtime_label = ttk.Label(self, text="Downtime based on Overall SLA:")
        downtime_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        # Treeview for displaying downtime
        downtime_columns = ("SLA", "Downtime per week", "Downtime per month", "Downtime per year")
        self.downtime_tree = ttk.Treeview(self, columns=downtime_columns, show="headings", selectmode="browse")

        for col in downtime_columns:
            self.downtime_tree.heading(col, text=col)
        self.downtime_tree.grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

    def add_service(self):
        service = self.service_var.get()
        sla = self.sla_var.get()

        if service and sla:
            self.selected_services.append((service, float(sla)))
            self.service_var.set("")
            self.sla_var.set("")
            self.update_services_tree()
            self.calculate_downtime()
        
    def delete_service(self):
        selected_item = self.services_tree.selection()
        if selected_item:
            selected_index = self.services_tree.index(selected_item)
            del self.selected_services[selected_index]
            self.update_services_tree()
            self.calculate_downtime()

    def calculate_downtime(self):
        downtime_data = {
            "99%": {"week": 1.68, "month": 7.2, "year": 3.65 * 24},
            "99.9%": {"week": 10.1 / 60, "month": 43.2 / 60, "year": 8.76},
            "99.95%": {"week": 5 / 60, "month": 21.6 / 60, "year": 4.38},
            "99.99%": {"week": 1.01 / 60, "month": 4.32 / 60, "year": 52.56 / 60},
            "99.999%": {"week": 6 / 3600, "month": 25.9 / 3600, "year": 5.26 / 60},
        }

        self.downtime_tree.delete(*self.downtime_tree.get_children())

        for sla, downtime in downtime_data.items():
            self.downtime_tree.insert("", "end", values=(sla, downtime["week"], downtime["month"], downtime["year"]))

    def update_selected_sla(self, event):
        selected_service = self.service_var.get()
        if selected_service in self.component_slas:
            self.sla_var.set(str(self.component_slas[selected_service]))

    def update_services_tree(self):
        self.services_tree.delete(*self.services_tree.get_children())

        for service, sla in self.selected_services:
            self.services_tree.insert("", "end", values=(service, sla))

    def calculate_sla(self):
        try:
            composite_sla = 1.0

            for _, sla in self.selected_services:
                composite_sla *= sla / 100.0

            probability_of_failure = 1 - composite_sla

            self.result_var1.set(f"{composite_sla:.10f} or {composite_sla * 100:.8f}%")
            self.result_var2.set(f"{probability_of_failure:.10f} or {probability_of_failure * 100:.6f}%")
        except ValueError:
            self.result_var1.set("Invalid input. Please enter valid numbers.")
            self.result_var2.set("")

if __name__ == "__main__":
    app = CompositeSLACalculatorApp()
    app.mainloop()
