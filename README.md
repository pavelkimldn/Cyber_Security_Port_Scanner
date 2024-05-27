# Cyber_Security_Port_Scanner

The purpose of this project was to develop a simple port scanner using Python to identify open ports on a given IP address range. This tool can be invaluable for network security assessments, allowing users to identify potential vulnerabilities by discovering open ports that could be exploited by attackers. To demonstrate the functionality and effectiveness of the port scanner, I created sample data to run tests on the code. The results were then visualized using advanced techniques, including a heatmap of open ports by IP (fig 1), a 3D scatter plot of open ports (fig 2), and a distribution plot of open ports (fig 3). 

The 3D scatter plot visualizes the open ports identified by the port scanner across different IP addresses and port ranges. The x-axis represents the port numbers, the y-axis represents the IP addresses (using the last octet), and the z-axis indicates the count of open ports found on each IP address. Each point in the plot represents an open port detected on a specific IP address. The plot reveals a wide distribution of open ports across the port range (0 to 1000), with several clusters around certain port numbers, indicating common services or vulnerabilities. The IP addresses show even distribution, with some addresses having multiple open ports, highlighting potential targets for attackers. Concentrations of open ports in the lower range (0 to 400) suggest common usage for services like HTTP, FTP, or SSH, which are frequently targeted. These findings help identify vulnerabilities, prioritize security measures, and monitor services. By closing unused ports and enhancing firewall rules, network security can be significantly improved. This visualization demonstrates the importance of port scanning in network security assessments and the effectiveness of Python-based tools in identifying and visualizing open ports.
*Figure 1*

![github](https://github.com/pavelkimldn/Cyber_Security_Port_Scanner/blob/main/Picture%201.png)

*Figure 2*

![github](https://github.com/pavelkimldn/Cyber_Security_Port_Scanner/blob/main/Picture%202.png)

*Figure 2*

![github](https://github.com/pavelkimldn/Cyber_Security_Port_Scanner/blob/main/Picture%203.png)

