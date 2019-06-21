echo "==========================================================="
echo "BEGIN SCRIPT - FINAL PROJECT - DOING AWESOME THINGS"
echo "==========================================================="
# Clone the chart repo
# git clone https://github.com/hashicorp/consul-helm.git
sudo cd consul-helm

# Checkout a tagged version
sudo git checkout v0.1.0

# Run Helm
sudo helm install --name consul ./

echo "==========================================================="
echo "SCRIPT ENDED - FINAL PROJECT - CONSUL IS INSTALLED"
echo "==========================================================="
~                                                                  
