<template>
    <nav class="navbar">
      <ul class="nav-list">
        <RouterLink to="/">Configmaps</RouterLink>
      </ul>
    </nav>
</template>
  
  <style scoped>
  .navbar {
    background-color: #333;
    color: #fff;
    padding: 10px;
  }
  
  .nav-list {
    font-size: 25px;
    list-style: none;
    display: flex;
    gap: 20px;
    justify-content: flex-start;
    padding: 0;
    margin: 0;
  }
  
  .nav-item {
    margin: 0 10px;
  }
  
  </style>