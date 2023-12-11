module.exports = {
    apps: [{
      script: 'npm start'
    }],
  
    deploy: {
      production: {
        key: 'trumio-inter.pem',
        user: 'ubuntu',
        host: '35.89.252.50',
        ref: 'origin/main',
        repo: 'https://github.com/Pradeep-Kumar-Rebbavarapu/UPEC-SERVER.git',
        path: '/home/ubuntu',
        'pre-deploy-local': '',
        'post-deploy': 'source ~/.nvm/nvm.sh && cd client && npm install && npm run build && cd .. && pm2 reload ecosystem.config.js --env production',
        'pre-setup': '',
        'ssh_options': 'ForwardAgent=yes'
      }
    }
  };