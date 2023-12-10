'use client'
import { Inter } from 'next/font/google'
import './globals.css'
import React from 'react'
import NavbarComponent from '@/components/NavbarComponent/NavbarComponent'
import {
  useQuery,
  useMutation,
  useQueryClient,
  Hydrate,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import HomeContext, { HomeProvider } from '@/context/HomeContext'
const inter = Inter({ subsets: ['latin'] })
import toast, { Toaster } from 'react-hot-toast';
export default function RootLayout({ children }) {
  const [queryClient] = React.useState(() => new QueryClient())
  const imageDirectURL = `${process.env.SITE_URL}/upec-logo.png`
  return (

    <html lang="en">
      <head>
        <link rel="manifest" href="/manifest.webmanifest" />
        <link rel="apple-touch-icon" sizes="180x180" href="/favicon/apple-touch-icon.png" />
        <link rel="icon" type="image/png" sizes="32x32" href="/favicon/favicon-32x32.png" />
        <link rel="icon" type="image/png" sizes="16x16" href="/favicon/favicon-16x16.png" />

        <meta property="twitter:image" content={imageDirectURL} />
        <meta property="twitter:title" content="TRUMIO - A University Platform" />
        <meta property="twitter:description" content="TRUMIO - A University Platform" />

        <meta property="og:title" content="TRUMIO - A University Platform" />
        <meta property="og:description" content="TRUMIO - A University Platform" />
        <meta property="og:image" content={imageDirectURL} />
        <meta property="og:image:type" content="image/png" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:image:alt" content="TRUMIO - A University Platform" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content={process.env.SITE_URL} />

        <meta name="description" content="TRUMIO - A University Platform" />
        <meta itemprop="name" content="TRUMIO - A University Platform" />
        <meta itemprop="description" content="TRUMIO - A University Platform" />
        <meta itemprop="image" content={imageDirectURL} />
        <meta name="keywords" content="A University Driven PlatForm Where Students And Alumni From Different colleges Can Work Together" />
        <meta name="author" content="Your Name" />
        <meta name="robots" content="index, follow" />
      </head>
      <body className={inter.className}>

        <QueryClientProvider client={queryClient}>
          <HomeProvider>
            <NavbarComponent />
            <Toaster />
            {children}


          </HomeProvider>
          <ReactQueryDevtools initialIsOpen={false} />
        </QueryClientProvider>

      </body>
    </html>

  )
}
