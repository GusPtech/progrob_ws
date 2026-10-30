#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

// Nodo que escucha el topic "chatter" y muestra cada mensaje recibido
class SubscriberCpp : public rclcpp::Node {
public:
  SubscriberCpp() : Node("subscriber_cpp") {
    // Crea la suscripción: tipo String, topic "chatter", cola de 10 mensajes
    // Cada vez que llega un mensaje se ejecuta la función lambda
    subscription_ = this->create_subscription<std_msgs::msg::String>(
      "chatter", 10,
      [this](const std_msgs::msg::String::SharedPtr msg) {
        RCLCPP_INFO(this->get_logger(), "C++ recibió: '%s'", msg->data.c_str());
      });
  }

private:
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<SubscriberCpp>());
  rclcpp::shutdown();
  return 0;
}
