variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "subnet_cidr" {
  default = "10.0.1.0/24"
}

variable "instance_type" {
  description = "The type of EC2 instance to launch"
  default     = "t3.medium" # why - how to measure capacity 
}

variable "key_name" {
  description = "Name of the SSH key to use for the instance"
  default     = "project"
}

variable "ami_id" {
  description = "The AMI ID to use for the EC2 instance (Ubuntu)"
  default     = "ami-0866a3c8686eaeeba" # Ubuntu 
}
