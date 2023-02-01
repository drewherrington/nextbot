<template>
    <div class="container mx-auto">
        <div class="flex items-start justify-center max-w-6xl mx-auto">
            <div class="w-4/5 marker:flex-1">
                <div class="w-full border border-gray-200 rounded-xl bg-white my-4">
                    <div class="relative w-full p-6 overflow-y-auto">
                        <div class="space-y-3">
                            <div v-for="(order, index) in orders" :key="index" class="flex items-start border border-gray-200 bg-gray-50 rounded-xl p-4">
                                <div>
                                    <div class="h-32 w-32 bg-gray-200 rounded-lg"></div>
                                </div>

                                <div class="ml-4">
                                    <div class="mb-3">
                                        <span class="text-base font-semibold text-gray-800">Order #{{ order.number }}</span>
                                    </div>

                                    <dl>
                                        <div class="bg-transparent py-1 sm:grid sm:grid-cols-3 sm:gap-4">
                                            <dt class="text-sm font-medium text-gray-500 sm:col-span-2">Item(s) Subtotal</dt>
                                            <dd class="mt-1 text-sm text-gray-800 sm:mt-0">{{ order.subtotal }}</dd>
                                        </div>

                                        <div class="bg-transparent py-1 sm:grid sm:grid-cols-3 sm:gap-4">
                                            <dt class="text-sm font-medium text-gray-500 sm:col-span-2">Postage and Packaging</dt>
                                            <dd class="mt-1 text-sm text-gray-800 sm:mt-0">{{ order.postage }}</dd>
                                        </div>

                                        <div class="bg-transparent py-1 sm:grid sm:grid-cols-3 sm:gap-4">
                                            <dt class="text-sm font-bold text-gray-900 sm:col-span-2">Total</dt>
                                            <dd class="mt-1 text-sm font-bold text-gray-800 sm:mt-0">{{ order.total }}</dd>
                                        </div>
                                    </dl>
                                </div>

                                <div class="ml-4 flex flex-1 justify-end h-full">
                                    <span :class="{ 'bg-red-100 text-red-700 border-red-200': order.status === 'Canceled' }" class="text-xs font-semibold bg-gray-100 border border-gray-200 rounded-full py-1 px-2">
                                        {{ order.status }}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="ml-6 w-2/5">
                <div class="w-full border border-gray-200 rounded-xl bg-white my-4">
                    <div class="relative w-full p-6 overflow-y-auto h-[40rem]">
                        <ul class="space-y-3">
                            <li v-for="(message, index) in messages" :key="index">
                                <div v-if="message.user === 'bot'" class="relative mr-auto w-3/4 px-4 py-2 text-white bg-blue-500 rounded-xl shadow-sm">
                                    <span class="block">{{ message.body }}</span>
                                </div>

                                <div v-else class="relative ml-auto w-3/4 px-4 py-2 text-gray-700 bg-gray-100 rounded-xl shadow-sm">
                                    <span class="block">{{ message.body }}</span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <form @submit.prevent="postMessage" class="flex items-center justify-between w-full p-3 border-t border-gray-300">
                        <input v-model="body" type="text" placeholder="Message"
                        class="block w-full py-2 pl-4 mx-3 bg-gray-100 rounded-full outline-none focus:text-gray-700"
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
