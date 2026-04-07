// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from autopatrol_interfaces:srv/SpeechText.idl
// generated code does not contain a copyright notice

#ifndef AUTOPATROL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__BUILDER_HPP_
#define AUTOPATROL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "autopatrol_interfaces/srv/detail/speech_text__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace autopatrol_interfaces
{

namespace srv
{

namespace builder
{

class Init_SpeechText_Request_text
{
public:
  Init_SpeechText_Request_text()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autopatrol_interfaces::srv::SpeechText_Request text(::autopatrol_interfaces::srv::SpeechText_Request::_text_type arg)
  {
    msg_.text = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autopatrol_interfaces::srv::SpeechText_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::autopatrol_interfaces::srv::SpeechText_Request>()
{
  return autopatrol_interfaces::srv::builder::Init_SpeechText_Request_text();
}

}  // namespace autopatrol_interfaces


namespace autopatrol_interfaces
{

namespace srv
{

namespace builder
{

class Init_SpeechText_Response_result
{
public:
  Init_SpeechText_Response_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::autopatrol_interfaces::srv::SpeechText_Response result(::autopatrol_interfaces::srv::SpeechText_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::autopatrol_interfaces::srv::SpeechText_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::autopatrol_interfaces::srv::SpeechText_Response>()
{
  return autopatrol_interfaces::srv::builder::Init_SpeechText_Response_result();
}

}  // namespace autopatrol_interfaces

#endif  // AUTOPATROL_INTERFACES__SRV__DETAIL__SPEECH_TEXT__BUILDER_HPP_
