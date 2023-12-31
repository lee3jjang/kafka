import { Controller } from '@nestjs/common';
import { EventPattern, MessagePattern } from '@nestjs/microservices';

@Controller()
export class AppController {
  @EventPattern('topic_1')
  async handleTopic(data) {
    console.log(data);
  }
}
