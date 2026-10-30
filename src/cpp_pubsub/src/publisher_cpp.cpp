#include <chrono>
#include <string>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

// Nodo que publica un mensaje de texto cada 500 ms en el topic "chatter"
class PublisherCpp : public rclcpp::Node {
public:
  PublisherCpp() : Node("publisher_cpp"), count_(0) {
    // Crea el publisher: tipo String, topic "chatter", cola de 10 mensajes
    publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);
    // Crea un temporizador que llama a timer_callback cada 500 ms
    timer_ = this->create_wall_timer(
      500ms, std::bind(&PublisherCpp::timer_callback, this));
  }

private:
  void timer_callback() {
    auto msg = std_msgs::msg::String();
    msg.data = "Hola desde C++ #" + std::to_string(count_++);
    RCLCPP_INFO(this->get_logger(), "Publicando: '%s'", msg.data.c_str());
    publisher_->publish(msg);
  }

  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char * argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PublisherCpp>());
  rclcpp::shutdown();
  return 0;
}
