resource "aws_vpc" "depi_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true # Enable DNS support
  enable_dns_hostnames = true # Enable DNS hostnames
  tags = {
    Name = "DEPI_VPC"
  }
}

resource "aws_subnet" "depi_subnet" {
  vpc_id            = aws_vpc.depi_vpc.id
  cidr_block        = var.subnet_cidr
  availability_zone = "us-east-1a"

  tags = {
    Name = "DEPI-Subnet"
  }
}

resource "aws_internet_gateway" "depi_igw" {
  vpc_id = aws_vpc.depi_vpc.id

  tags = {
    Name = "DEPI-IGW"
  }
}

resource "aws_route_table" "main_route_table" {
  vpc_id = aws_vpc.depi_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.depi_igw.id
  }
  tags = {
    Name = "DEPI-RouteTable"
  }
}

resource "aws_route_table_association" "main_route_association" {
  subnet_id      = aws_subnet.depi_subnet.id
  route_table_id = aws_route_table.main_route_table.id
}
