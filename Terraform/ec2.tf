resource "aws_instance" "depi_instance" {
  ami                         = var.ami_id
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.depi_subnet.id
  key_name                    = var.key_name
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.app_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install -y nginx
              echo "<html><head><title>DEPI Team</title></head><body><h1>Hello DEPI Team</h1></body></html>" | sudo tee /var/www/html/index.html
              sudo service nginx start
              EOF
  root_block_device {
    volume_size = 35    
    volume_type = "gp2" #why  # General Purpose SSD
  }
  tags = {
    Name = "DEPI-Frontend"  
  }
}
