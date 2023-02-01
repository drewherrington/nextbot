<template>
    <div class="container mx-auto">
        <div class="flex-col items-center justify-center w-full">
            <div class="mt-6 text-center">
                <h2 class="text-gray-50 font-bold text-3xl">NextBot</h2>
            </div>

            <div class="w-1/2 mx-auto">
                <div class="w-full border border-gray-700 rounded-xl bg-gray-600 my-4">
                    <div class="relative w-full p-6 overflow-y-auto h-[40rem]">
                        <ul class="space-y-3">
                            <li v-for="(message, index) in messages" :key="index">
                                <div v-if="message.user === 'bot'" class="relative mr-auto w-1/4 px-4 py-2 text-white bg-gray-500 rounded-xl shadow-sm">
                                    <span class="block">{{ message.body }}</span>
                                </div>

                                <div v-else class="relative ml-auto w-1/4 px-4 py-2 text-gray-700 bg-gray-100 rounded-xl shadow-sm">
                                    <span class="block">{{ message.body }}</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <form @submit.prevent="postMessage" class="flex items-center justify-between w-full p-3 border-t border-gray-700">
                        <input v-model="body" type="text" placeholder="Message"
                        class="block w-full py-2 pl-4 mx-3 bg-gray-500 rounded-full outline-none focus:text-gray-100"
                        name="message" required />

                        <button type="submit">
                            <svg class="w-5 h-5 text-gray-500 origin-center transform rotate-90" xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 20 20" fill="currentColor">
                            <path
                            d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
                            </svg>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    data () {
        return {
            messages: [] as any,
            body: null,
            orderNumber: null,
            orders: [
                {
                    number: '9175898',
                    subtotal: '£7.49',
                    postage: '£0.00',
                    total: '£7.49',
                    status: 'Pending'
                },
                {
                    number: '3433938',
                    subtotal: '£12.99',
                    postage: '£3.00',
                    total: '£15.99',
                    status: 'Pending'
                },
                {
                    number: '0757371',
                    subtotal: '£17.66',
                    postage: '£0.00',
                    total: '£17.66',
                    status: 'Pending'
                }
            ]
        };
    },

    methods: {
        postMessage () {
            if (this.isOrderNumber(this.body)) {
                this.orderNumber = this.body;
            }

            this.messages.push({
                user: 'customer',
                body: this.body ?? '',
                postedAt: new Date(Date.now())
            });

            axios.post('http://127.0.0.1:5000', { body: this.body })
                .then(response => {
                    this.messages.push({
                        user: 'bot',
                        body: response.data,
                        postedAt: new Date(Date.now())
                    });

                    this.analyseResponse(response.data);

                    this.body = null;
                })
                .catch(error => alert(error));
        },

        isOrderNumber (number: string | null) {
            let exists = false;

            if (number === null) {
                return exists;
            }

            this.orders.forEach((order: any) => {
                if (order.number === number) {
                    exists = true;
                }
            });

            return exists;
        },

        analyseResponse (response: string) {
            if (response == 'Your order has been canceled') {
                this.cancelOrder(this.orderNumber);
            }
        },

        cancelOrder (number: string | null) {
            if (number === null) {
                return;
            }

            this.orders = this.orders.map(order => {
                if (order.number === number) {
                    order.status = 'Canceled';
                }

                return order;
            });
        }
    }
});
</script>
