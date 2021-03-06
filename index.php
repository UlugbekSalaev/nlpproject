<?php 
	$menu="home";
	if(isset($_GET["menu"])) $menu=$_GET["menu"];
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>UrSU NLP</title>

  <!-- Google Font: Source Sans Pro -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="./plugins/fontawesome-free/css/all.min.css">
  <!-- overlayScrollbars -->
  <link rel="stylesheet" href="./plugins/overlayScrollbars/css/OverlayScrollbars.min.css">
  <!-- Theme style -->
  <link rel="stylesheet" href="./dist/css/adminlte.min.css">
</head>
<body class="hold-transition sidebar-mini layout-fixed">
<!-- Site wrapper -->
<div class="wrapper">
  <!-- Navbar -->
  <nav class="main-header navbar navbar-expand navbar-white navbar-light">
    <!-- Left navbar links -->
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="./?menu=home" class="nav-link">Home</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="./?menu=news" class="nav-link">News</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="./?menu=publications" class="nav-link">Publications</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="./?menu=team_members" class="nav-link">Team Members</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="./?menu=collaborators" class="nav-link">Collaborators</a>
      </li>
    </ul>

    <!-- SEARCH FORM -->
    <form class="form-inline ml-3">
      <div class="input-group input-group-sm">
        <input class="form-control form-control-navbar" type="search" placeholder="Search" aria-label="Search">
        <div class="input-group-append">
          <button class="btn btn-navbar" type="submit">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
    </form>

    <!-- Right navbar links -->
    <ul class="navbar-nav ml-auto">
      
      <li class="nav-item">
        <a class="nav-link" data-widget="fullscreen" href="#" role="button">
          <i class="fas fa-expand-arrows-alt"></i>
        </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" data-widget="control-sidebar" data-slide="true" href="#" role="button">
          <i class="fas fa-th-large"></i>
        </a>
      </li>
    </ul>
  </nav>
  <!-- /.navbar -->

  <!-- Main Sidebar Container -->
  <aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <a href="./" class="brand-link">
      <img src="./dist/img/urdu_logo.png" alt="UrSU" class="brand-image img-circle elevation-3" style="opacity: .8">
      <span class="brand-text font-weight-light">UrSU NLP Projects</span>
    </a>

    <!-- Sidebar -->
    <div class="sidebar">
      <!-- Sidebar user (optional) -->
      <!--<div class="user-panel mt-3 pb-3 mb-3 d-flex">
        <div class="image">
          <img src="./dist/img/urdu_logo.png" class="img-circle elevation-2" alt="UrSU">
        </div>
        <div class="info">
          <a href="#" class="d-block">NLP Team</a>
        </div>
      </div>-->

      <!-- SidebarSearch Form -->
      <div class="form-inline">
        <div class="input-group" data-widget="sidebar-search">
          <input class="form-control form-control-sidebar" type="search" placeholder="Search" aria-label="Search">
          <div class="input-group-append">
            <button class="btn btn-sidebar">
              <i class="fas fa-search fa-fw"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- Sidebar Menu -->
      <nav class="mt-2">
        <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">

		  <li class="nav-item menu-open">
            <a href="#" class="nav-link active">
              <i class="nav-icon fas fa-copy"></i>
              <p>
                Tools
                <i class="fas fa-angle-left right"></i>
                <span class="badge badge-info right">8</span>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="./?menu=translit" class="nav-link <?=($menu=='translit')?'active':'';?>">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Transliteration</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="./" class="nav-link">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Visualization</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="./" class="nav-link">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Sentiment analysis</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="./" class="nav-link">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Text Classification </p>
                </a>
              </li>
              <li class="nav-item">
                <a href="./" class="nav-link">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Morphological analysis</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="./" class="nav-link">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Stemmer</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="./" class="nav-link">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Dictionary</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="./" class="nav-link">
                  <i class="far fa-circle nav-icon"></i>
                  <p>Resources</p>
                </a>
              </li>
            </ul>
          </li>
        </ul>
      </nav>
      <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->
  </aside>

  <!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper">
    <!-- Main content -->
    <?php 
		if(!file_exists($menu.".php")) $menu="home";
		include_once($menu.".php");
	?>
    <!-- /.Main content -->
  </div>
  <!-- /.content-wrapper -->

  <footer class="main-footer">
    <div class="float-right d-none d-sm-block">
      Version 1.0
    </div>
    Copyright &copy; 2022 <a href="https://urdu.uz">UrSU NLP Team</a>. All rights reserved.
  </footer>

  <!-- Control Sidebar -->
  <aside class="control-sidebar control-sidebar-dark">
    <!-- Control sidebar content goes here -->
  </aside>
  <!-- /.control-sidebar -->
</div>
<!-- ./wrapper -->

<!-- jQuery -->
<script src="./plugins/jquery/jquery.min.js"></script>
<!-- Bootstrap 4 -->
<script src="./plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<!-- overlayScrollbars -->
<script src="./plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js"></script>
<!-- AdminLTE App -->
<script src="./dist/js/adminlte.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="./dist/js/demo.js"></script>
</body>
</html>